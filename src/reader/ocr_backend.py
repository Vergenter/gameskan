from typing import Optional, Protocol
from abc import abstractmethod
from reader.bounds import Bounds

from reader.text_field import TextField


class OCRBackend(Protocol):
    @abstractmethod
    def read_text(
        self, img, bounds: Optional[Bounds]) -> set[TextField]: raise NotImplementedError
