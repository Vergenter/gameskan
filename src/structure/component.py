from dataclasses import dataclass
from model.bounds import Bounds
from typing import Protocol,Union
from abc import abstractmethod
from ocr_backend.text_field import TextField
import ocr_backend.Iocr_backend
import ocr_backend.ocr
import oir_backend.Ioir_backend
import oir_backend.oir
import numpy as np
from model.image import Image
@dataclass(frozen=True)
class Component(Protocol):
    @abstractmethod
    def map(self,image:Image)->Union[list[TextField],list[Bounds]]: raise NotImplementedError

@dataclass(frozen=True)
class Component:
    bounds:Bounds
    ocr_method:ocr_backend.Iocr_backend.IOCRBackend=ocr_backend.ocr.OCR()
    def map(self,image:Image)->list[TextField]:
        return self.ocr_method.get_text(image)
@dataclass(frozen=True)
class Component:
    bounds:Bounds
    asset:np.ndarray
    oir_method:oir_backend.Ioir_backend.IOIRBackend=oir_backend.oir.OIR()
    # match_asset
    def map(self,image:Image)->list[TextField]:
        return self.oir_method.match_asset(image,self.asset)
