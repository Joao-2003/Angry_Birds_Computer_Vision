from abc import ABC, abstractmethod


class GameState(ABC):

    def __init__(self, game):
        self.game = game

    @abstractmethod
    def handle_input(self, event):
        return

    @abstractmethod
    def update(self):
        return
