from typing import Protocol
from abc import abstractmethod
from src.reader.bounds import Bounds

from src.reader.text_field import TextField


class OCRBackend(Protocol):
    @abstractmethod
    def read_text(
        self, img, bounds: Bounds) -> set[TextField]: raise NotImplementedError
