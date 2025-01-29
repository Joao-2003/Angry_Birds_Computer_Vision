from abc import ABC, abstractmethod


class Size(ABC):

    @abstractmethod
    def get_mass(self) -> float:
        return

    @abstractmethod
    def get_radius(self) -> float:
        return

    @abstractmethod
    def get_life(self) -> int:
        return