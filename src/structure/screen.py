from dataclasses import dataclass, field
from structure.component import ComponentResult
from structure.layer import Layer
from model.image import Image
from operator import methodcaller

ScreenResult = list[list[ComponentResult]]


class Screen:
    """App view differentiating for which component to look"""

    def __init__(self, identifing_layer: Layer, layers: list[Layer]):
        self.identifing_layer = identifing_layer
        self.layers = layers
        self._identifing_layer: list[ComponentResult] = []

    def indentify(self, image: Image):
        self._identifing_layer = self.identifing_layer.map(image)
        return all(self._identifing_layer)

    def map(self, image: Image) -> ScreenResult:
        return (self._identifing_layer, *[layer.map(image) for layer in self.layers])
