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

        sharp5 = np.array([
            [-1, -1, -1, -1, -1],
            [-1, +1, +2, +1, -1],
            [-1, +2, +4, +2, -1],
            [-1, +1, +2, +1, -1],
            [-1, -1, -1, -1, -1]
        ])

        scaled_templates = [asset]
        base = img

        def split_by_colour(_img):
            return _img[:, :, 0], _img[:, :, 1], _img[:, :, 2]

        bounds = []
        r, g, b = split_by_colour(base)
        methods = [cv.TM_CCOEFF_NORMED]
        methods_names = ["cv.TM_CCOEFF_NORMED"]
        for templates_split_by_color in map(split_by_colour, scaled_templates):
            result_color = None
            for color, base_color, template_color in zip(("red", "green", "blue"), (r, g, b), templates_split_by_color):
                w, h = template_color.shape[::-1]
                for name, method in zip(methods_names, methods):
                    res = cv.matchTemplate(
                        base_color, template_color, method, mask=asset[:, :, 3])
                    if result_color is not None:
                        result_color += res
                    else:
                        result_color = res
            result_color /= 3
            fig, ax = plt.subplots(1, 5)
            img_copy = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            ax[0].imshow(img_copy, cmap='gray')
            cv.normalize(result_color, result_color, 0.0,
                         1.0, cv.NORM_MINMAX, cv.CV_32FC1)
            ax[1].imshow(result_color, cmap='gray')
            _, treesholded = cv.threshold(
                result_color, threshold, 1, cv.THRESH_BINARY)
            ax[2].imshow(treesholded, cmap='gray')

            sharpen_img = cv.filter2D(result_color, -1, sharp5)

            ax[3].imshow(treesholded, cmap='gray')
            loc = np.where(sharpen_img >= threshold)

            for pt in zip(*loc[::-1]):
                img_copy = cv.rectangle(
                    img_copy, (pt[0], pt[1]), (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                bounds.append(Bounds(pt[0], pt[1], pt[0] + w, pt[1] + h))
            ax[4].imshow(img_copy, cmap='gray')
        return bounds
