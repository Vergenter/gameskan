from dataclasses import dataclass
from functools import cached_property
from typing import Tuple


@dataclass(frozen=True)
class Bounds:
    """Class to specify bounds of items"""
    box_x: int = 0
    box_y: int = 0
    box_x_len: int = 0
    box_y_len: int = 0

    @cached_property
    def center(self) -> Tuple[float, float]:
        return (self.box_x+self.box_x_len/2, self.box_y+self.box_y_len/2)
