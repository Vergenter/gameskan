from typing import Protocol
from abc import abstractmethod
from model.image import Image
from structure.screen import Screen, ScreenResult


class Ireader(Protocol):
    @abstractmethod
    def read(
            self, img: Image, screens: list[Screen]) -> list[ScreenResult]:
        raise NotImplementedError
