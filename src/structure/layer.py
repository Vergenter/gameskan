from dataclasses import dataclass
from structure.component import Component, ComponentResult
from model.image import Image
from operator import methodcaller


class Layer:
    def __init__(self, components: list[Component]):
        self.components = components

    # is_tranparent: bool
    # is_optional: bool

    def map(self, image: Image) -> list[ComponentResult]:
        return [component.map(image) for component in self.components]
