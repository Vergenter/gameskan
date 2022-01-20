from ocr_backend import OCRBackend
from ocr_backend import Bounds
from reader.text_field import TextField
from PIL.Image import Image

from tesserocr import PyTessBaseAPI, RIL #https://github.com/sirfz/tesserocr/blob/master/tesserocr.pyx

class OCR(OCRBackend):
    
    def __init__(self) -> None:
        pass

    def read_text(self, img: Image, bounds: Bounds = None) -> set[TextField]:
        tmp = []
        with PyTessBaseAPI(lang='eng+pol') as api:
            api.SetImage(img)
            boxes = api.GetComponentImages(RIL.TEXTLINE, True) # TEXTLINE, WORD, SYMBOL, PARA, BLOCK
            for i, (im, box, _, _) in enumerate(boxes):
                if bounds:
                    api.SetRectangle(bounds.box_x, bounds.box_y, bounds.box_x_len, bounds.box_y_len)
                else: 
                    api.SetRectangle(box['x'], box['y'], box['w'], box['h'])
                ocrResult = api.GetUTF8Text()
                tmp.append(ocrResult)
        return set(tmp)



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
