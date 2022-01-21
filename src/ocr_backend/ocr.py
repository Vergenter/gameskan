from ocr_backend.Iocr_backend import IOCRBackend
from model.bounds import Bounds
from ocr_backend.text_field import TextField
from model.image import Image

# https://github.com/sirfz/tesserocr/blob/master/tesserocr.pyx
from tesserocr import PyTessBaseAPI, RIL


class OCR(IOCRBackend):

    def __init__(self) -> None:
        pass

    def get_text(self, img: Image, bounds: Bounds = None, lang: str = 'eng+pl') -> set[TextField]:
        result = []
        with PyTessBaseAPI(lang=lang) as api:
            api.SetImage(img.pilImage)
            # TEXTLINE, WORD, SYMBOL, PARA, BLOCK
            boxes = api.GetComponentImages(RIL.TEXTLINE, True)
            for i, (im, box, _, _) in enumerate(boxes):
                if bounds:
                    api.SetRectangle(bounds.box_x, bounds.box_y,
                                     bounds.box_x_len, bounds.box_y_len)
                else:
                    api.SetRectangle(box['x'], box['y'], box['w'], box['h'])
                ocrResult = api.GetUTF8Text()
                result.append(ocrResult)
        return [TextField(bounds, res) for res in result]


# from PIL import Image
# import cv2 as cv
# img_path = 'screens/1080x2310/mainmenu.jpg'
# img_pil = Image.open(img_path)
# print(img_pil)
# img = cv.imread(img_path)
# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# ocr = OCR()
# test = ocr.read_text(img)
# print(test)
