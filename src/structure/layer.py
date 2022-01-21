from dataclasses import dataclass
from structure.component import Component


@dataclass(frozen=True)
class Layer:
    components:list[Component]
    is_tranparent:bool
    is_optional:bool
