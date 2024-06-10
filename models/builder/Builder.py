from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_type(self) -> None:
        pass

    @abstractmethod
    def produce_position(self) -> None:
        pass

    @abstractmethod
    def produce_speed(self) -> None:
        pass
    
    @abstractmethod
    def produce_sprite(self) -> None:
        pass
    
    @abstractmethod
    def produce_rect(self) -> None:
        pass
    
    @abstractmethod
    def produce_direction(self) -> None:
        pass