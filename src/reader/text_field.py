from dataclasses import dataclass
from functools import cached_property

from reader.bounds import Bounds


@dataclass(frozen=True)
class TextField:
    """Class for keeping track of an item in inventory."""
    bounds: Bounds
    text: str = ""

    @cached_property
    def __hash__(self):
        return hash(self.text)
