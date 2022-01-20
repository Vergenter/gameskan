import numpy as np
import cv2
from PIL import Image


def toImgOpenCV(imgPIL: Image) -> np.ndarray:  # Conver imgPIL to imgOpenCV
    i = np.array(imgPIL)  # After mapping from PIL to numpy : [R,G,B,A]
    # numpy Image Channel system: [B,G,R,A]
    red = i[:, :, 0].copy()
    i[:, :, 0] = i[:, :, 2].copy()
    i[:, :, 2] = red
    return i


def toImgPIL(imgOpenCV: np.ndarray) -> Image:
    return Image.fromarray(cv2.cvtColor(imgOpenCV, cv2.COLOR_BGR2RGB))
