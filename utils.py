import cv2 as cv  # 4.5.5
from typing import Optional
from matplotlib import pyplot as plt
from glob import glob
import numpy as np


def show_image(img, title: Optional[str] = None):
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    if title:
        plt.title(title)
    plt.show()

def load_test_assets():
    assets_dict = {
        'altars': ['dung_altar.1.png', 'dung_altar.2.png', 'dung_altar.3.png', 'dung_altar_used.png'],
        'ladder': ['dung_ladderdown.png'],
        'monsters': ['mon_bomb.png', 'mon_bow.png', 'mon_wizard.png', 'mon_bomb_cd.png', 'mon_sword.png', 'mon_wizard_cd.png'],
        'player': ['player_fleece.png', 'player_nospear.png', 'player_nospear_fleece.png'],
        'floors': ['tile_base.png', 'tile_floor.1.png', 'tile_floor.2.png', 'tile_floor_large.1.png', 'tile_floor_large.2.png'],
        'liquids': ['tile_liquid.1.png', 'tile_liquid.2.png', 'tile_liquid.3.png', 'tile_liquid_large.1.png', 'tile_liquid_large.2.png', 'tile_liquid_large.3.png'],
    }

    assets_loaded = {}
    for key, array in assets_dict.items():
        assets_loaded[key] = []
        for path in array:
            assets_loaded[key].append(glob('output/'+path)[0])
    return assets_loaded

def bgra2rgba(img):
    return cv.cvtColor(img, cv.COLOR_BGRA2RGBA)




def resize_image(img, scale: int, interpolation: Optional[int] = cv.INTER_AREA):
    scale_percent = scale * 100 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv.resize(img, dim, interpolation = interpolation)

def plt_img(img: np.array, title: Optional[str] = None, cmap: Optional[str] = None):
    if cmap:
        plt.imshow(img, cmap=cmap)
    else:
        plt.imshow(img)
    if title:
        plt.title(title)
    plt.show()