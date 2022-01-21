from typing import Protocol, Optional
from abc import abstractmethod
from model.bounds import Bounds
from model.image import Image
from numpy import ndarray


class IOIRBackend(Protocol):
    @abstractmethod
    def match_asset(self, img: Image,
             asset: ndarray, threshold: Optional[float]) -> list[Bounds]: raise NotImplementedError
