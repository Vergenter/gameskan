from dataclasses import dataclass
from functools import cached_property


@dataclass(frozen=True, slots=True)
class Bounds:
    """Class to specify bounds of items"""
    box_x: int = 0
    box_y: int = 0
    box_x_len: int = 0
    box_y_len: int = 0
