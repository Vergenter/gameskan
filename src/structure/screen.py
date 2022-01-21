from dataclasses import dataclass
from structure.component import Component
from structure.layer import Layer


@dataclass(frozen=True)
class Screen:
    """App view differentiating for which component to look"""
    identifing_components: list[Component]
    layers: list[Layer]

    def indentify(self):
        return
    def map(self):
