from typing import Protocol
from abc import abstractmethod
from model.bounds import Bounds
from PIL.Image import Image
from numpy import ndarray

class OIRBackend(Protocol):
    @abstractmethod
    def show(self, img: ndarray, asset: ndarray) -> Bounds: raise NotImplementedError