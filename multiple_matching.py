import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import utils


templates_path = [
    "output/tile_base.png",
    "output/tile_liquid.2.png",
    "output/tile_floor.1.png",
    "output/tile_liquid.3.png",
    "output/tile_floor.2.png",
    "output/tile_liquid_large.1.png",
    "output/tile_floor_large.1.png",
    "output/tile_liquid_large.2.png",
    "output/tile_floor_large.2.png",
    "output/tile_liquid_large.3.png",
    "output/tile_liquid.1.png"
    ]
def scale_image(scale):
    def f(img):
        width = int(img.shape[1] * scale / 100)
        height = int(img.shape[0] * scale / 100)
        dim = (width, height)
        return cv.resize(img, dim, interpolation = cv.INTER_AREA)
    return f
templates = map(lambda x:cv.imread(x,0),templates_path)
scaled_templates = map(scale_image(400),templates)
base = cv.imread('screens/1080x1920/simple1.png')
img_gray = cv.cvtColor(base, cv.COLOR_BGR2GRAY)

for template in scaled_templates:  
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED,mask=template)
    threshold = 0.6
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        base = cv.rectangle(base, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)


utils.show_image(base)


