from abc import ABC, abstractmethod


class CharacterFactory(ABC):
    @abstractmethod
    def create_character(self, *args, **kwargs):
        return
