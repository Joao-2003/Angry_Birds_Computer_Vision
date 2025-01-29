import time
import pygame
from GameState import GameState


class LevelPausedState(GameState):

    def handle_input(self, event):
        self.game.mouse_pressed = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            self.game.set_state(self.game.playing_state)

    def update(self):
        self.check_level_cleared()
        self.check_level_failed()

    def check_level_cleared(self):
        if self.game.level.number_of_birds >= 0 and len(self.game.pigs) == 0:
            if self.game.bonus_score_once:
                self.game.score += (self.game.level.number_of_birds - 1) * 10000
            self.game.bonus_score_once = False
            self.game.set_state(self.game.level_cleared_state)

    def check_level_failed(self):
        if self.game.level.number_of_birds <= 0 < len(self.game.pigs):
            if time.time() - self.game.t2 > 6:
                self.game.set_state(self.game.level_failed_state)
