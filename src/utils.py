import numpy as np
import cv2
import PIL.Image


def toImgOpenCV(imgPIL: PIL.Image.Image) -> np.ndarray:  # Conver imgPIL to imgOpenCV
    i = np.array(imgPIL)  # After mapping from PIL to numpy : [R,G,B,A]
    # numpy Image Channel system: [B,G,R,A]
    red = i[:, :, 0].copy()
    i[:, :, 0] = i[:, :, 2].copy()
    i[:, :, 2] = red
    return i


def toImgPIL(imgOpenCV: np.ndarray) -> PIL.Image.Image:
    return PIL.Image.fromarray(cv2.cvtColor(imgOpenCV, cv2.COLOR_BGR2RGB))


def scale_image(cvImage: np.ndarray, scale: float) -> np.ndarray:
    scale_percent = scale * 100  # percent of original size
    width = int(cvImage.shape[1] * scale_percent / 100)
    height = int(cvImage.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(cvImage, dim, interpolation=cv2.INTER_AREA)
