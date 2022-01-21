from dataclasses import dataclass
from model.bounds import Bounds
from typing import Protocol, Union
from abc import abstractmethod
from ocr_backend.text_field import TextField
import ocr_backend.Iocr_backend
import ocr_backend.ocr
import oir_backend.Ioir_backend
import oir_backend.oir
import numpy as np
from model.image import Image

ComponentResult = Union[list[TextField], list[Bounds]]


@dataclass(frozen=True)
class Component(Protocol):
    @abstractmethod
    def map(self, image: Image) -> ComponentResult: raise NotImplementedError


class Component_OCR(Component):
    def __init__(self, bounds: Bounds, filter_text: str = None, ocr_method: ocr_backend.Iocr_backend.IOCRBackend = ocr_backend.ocr.OCR()):
        self.bounds = bounds
        self.filter_text = filter_text
        self.ocr_method = ocr_method

    def map(self, image: Image) -> list[TextField]:
        result: list[TextField] = self.ocr_method.get_text(image)
        if self.filter_text:
            return [x for x in result if self.filter_text in x.text]
        return result


class Component_OIR(Component):
    def __init__(self, bounds: Bounds, asset: np.ndarray, oir_method: oir_backend.Ioir_backend.IOIRBackend = oir_backend.oir.OIR()):
        self.bounds = bounds
        self.asset = asset
        self.oir_method = oir_method

    def map(self, image: Image) -> list[Bounds]:
        return self.oir_method.match_asset(image, self.asset)
