import pygame
from GameState import GameState


class LevelClearedState(GameState):

    def handle_input(self, event):
        self.game.mouse_pressed = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.game.x_mouse > 610 and self.game.y_mouse > 450:
                    self.game.level.restart()
                    self.game.level.load_level(self.game.level.number + 1)
                    self.game.set_state(self.game.playing_state)
                    self.game.score = 0
                    self.game.bird_path = []
                    self.game.bonus_score_once = True
                elif 500 < self.game.x_mouse < 610:
                    if self.game.y_mouse > 450:
                        self.game.level.restart()
                        self.game.level.load_level(self.game.level.number)
                        self.game.set_state(self.game.playing_state)
                        self.game.score = 0
                        self.game.bird_path = []

    def update(self):
        return
