from dataclasses import dataclass
from functools import cached_property

from src.reader.bounds import Bounds


@dataclass(frozen=True, slots=True)
class TextField:
    """Class for keeping track of an item in inventory."""
    text: str = ""
    bounds: Bounds

    @cached_property
    def __hash__(self):
        return hash(self.text)
