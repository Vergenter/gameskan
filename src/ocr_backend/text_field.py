from dataclasses import dataclass

from model.bounds import Bounds


@dataclass(frozen=True)
class TextField:
    """Class for keeping track of an item in inventory."""
    bounds: Bounds
    text: str = ""
