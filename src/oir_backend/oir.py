from msilib.schema import Class
import cv2 as cv
from oir_backend.Ioir_backend import IOIRBackend
from numpy import ndarray
from model.image import Image
import numpy as np
from model.bounds import Bounds
from matplotlib import pyplot as plt


class OIR(IOIRBackend):

    def __init__(self) -> None:
        pass

    def match_asset(self, img_wrapperd: Image, asset: ndarray, threshold: float = 0.8):
        img = img_wrapperd.cvImage
        print(asset.shape)

        # img = img_wrapperd.pilImage
        sharp5 = np.array([
            [-1, -1, -1, -1, -1],
            [-1, +1, +2, +1, -1],
            [-1, +2, +4, +2, -1],
            [-1, +1, +2, +1, -1],
            [-1, -1, -1, -1, -1]
        ])
        threshold = threshold

        scaled_templates = [asset]
        base = img

        def split_by_colour(_img):
            return _img[:, :, 0], _img[:, :, 1], _img[:, :, 2]
        fig, ax = plt.subplots(1,3)

        bounds = []
        r, g, b = split_by_colour(base)
        methods = [cv.TM_CCOEFF_NORMED]
        methods_names = ["cv.TM_CCOEFF_NORMED"]
        # cv.imshow('sd.jpg', base)
        for templates_split_by_color in map(split_by_colour, scaled_templates):
            result_color = None
            for color, base_color, template_color in zip(("red", "green", "blue"), (r, g, b), templates_split_by_color):
                w, h = template_color.shape[::-1]
                print('wh',w,h)
                print(base_color.shape)
                # ax[0].imshow(img, cmap='gray')

                for name, method in zip(methods_names, methods):
                    res = cv.matchTemplate(base_color, template_color, method, mask=asset[:,:,3])
                    print('res',res.shape)
                    if result_color is not None:
                        result_color += res
                    else:
                        result_color = res
            result_color /= 3
            ax[0].imshow(img, cmap='gray')
            # ax[0].imshow(img, cmap='gray')
            ax[1].imshow(result_color, cmap='gray')
            # plt.imwrite('x2.jpg', basee)

            sharpen_img = cv.filter2D(result_color, -1, sharp5)
            print('img', img.shape)
            print(result_color.shape)
            print(sharpen_img.shape)

            loc = np.where(sharpen_img >= threshold)
            # loc = np.where(result_color >= threshold)
            print(np.shape(loc))
            print(len(list(zip(*loc[::-1]))))
            # ax[2].imshow(result_color >= threshold, cmap='gray')
            # ax[2].imshow(list(zip(*loc[::-1])), cmap='gray')
            for pt in zip(*loc[::-1]):
                # bounds.append(Bounds(box_x=pt[0], box_y=pt[1], box_x_len=pt[0] + w, box_y_len=pt[1] + h))
                bounds.append(Bounds(pt[0], pt[1], pt[0] + w, pt[1] + h))


        return bounds


