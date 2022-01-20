from typing import Optional, Protocol
from abc import abstractmethod
from reader.bounds import Bounds
from PIL.Image import Image

from reader.text_field import TextField


class IOCRBackend(Protocol):
    @abstractmethod
    def read_text(
        self, img: Image, bounds: Optional[Bounds]) -> set[TextField]: raise NotImplementedError
