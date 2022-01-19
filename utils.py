import cv2 as cv  # 4.5.5
from typing import Optional
from matplotlib import pyplot as plt


def show_image(img, title: Optional[str] = None):
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    if title:
        plt.title(title)
    plt.show()
