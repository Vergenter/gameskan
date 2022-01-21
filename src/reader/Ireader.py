from typing import Protocol
from abc import abstractmethod
from model.bounds import Bounds
from PIL.Image import Image
from numpy import ndarray
from structure.screen import Screen


class Ireader(Protocol):
    @abstractmethod
    def match_asset(self, img: ndarray, screens: list[Screen]) -> list[Bounds]: raise NotImplementedError
