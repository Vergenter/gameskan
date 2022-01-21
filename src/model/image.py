from dataclasses import dataclass
from functools import cached_property
from typing import Tuple
import numpy as np
import PIL.Image
import model.bounds
import utils


@dataclass(frozen=True)
class Image:
    pilImage: PIL.Image.Image
    cvImage: np.array

    @classmethod
    def fromPIL(cls, pilImage: PIL.Image.Image):
        return cls(pilImage, utils.toImgOpenCV(pilImage))

    @classmethod
    def fromCV(cls, cvImage: np.ndarray):
        return cls(utils.toImgPIL(cvImage), cvImage)

    @cached_property
    def bounds(self) -> model.bounds.Bounds:
        # self.cvImage.shape[1] and self.cvImage.shape[0] reversed in cvImage
        return model.bounds.Bounds(0, 0, self.cvImage.shape[1], self.cvImage.shape[0])
