from typing import Protocol
from abc import abstractmethod


class OIRBackend(Protocol):
    @abstractmethod
    def show(self): raise NotImplementedError
