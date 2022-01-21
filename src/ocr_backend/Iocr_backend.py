from typing import Optional, Protocol
from abc import abstractmethod
from model.bounds import Bounds
from model.image import Image
from ocr_backend.text_field import TextField


class IOCRBackend(Protocol):
    @abstractmethod
    def get_text(
        self, img: Image, bounds: Optional[Bounds], lang: Optional[str]) -> list[TextField]: raise NotImplementedError
