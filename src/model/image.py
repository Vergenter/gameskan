from dataclasses import dataclass
from functools import cached_property
from typing import Tuple
import numpy as np
import PIL.Image
from utils import toImgOpenCV,toImgPIL
@dataclass(frozen=True)
class Image:
    pilImage : PIL.Image.Image
    cvImage: np.array
    @classmethod
    def fromPIL(cls, pilImage : PIL.Image.Image):
        return cls(pilImage,toImgOpenCV(pilImage))
    @classmethod
    def fromCV(cls, cvImage : np.ndarray):
        return cls(toImgPIL(cvImage),cvImage)

    