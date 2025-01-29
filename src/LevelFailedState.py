import pygame
from GameState import GameState


class LevelFailedState(GameState):

    def handle_input(self, event):
        self.game.mouse_pressed = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (500 < self.game.x_mouse < 620):
            if self.game.y_mouse > 450:
                self.game.level.restart()
                self.game.level.load_level(self.game.level.number)
                self.game.set_state(self.game.playing_state)
                self.game.bird_path = []
                self.game.score = 0

    def update(self):
        return
