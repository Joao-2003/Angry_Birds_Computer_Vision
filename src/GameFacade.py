from Game import Game
from WallObserver import WallObserver
from GravityObserver import GravityObserver


class GameFacade:

    def __init__(self):
        self.game = Game()
        self.wall_toggle_observer = WallObserver(self.game)
        self.gravity_toggle_observer = GravityObserver(self.game)
        self.game.subject.add_observer(self.wall_toggle_observer)
        self.game.subject.add_observer(self.gravity_toggle_observer)

    def run(self):
        self.game.run()
