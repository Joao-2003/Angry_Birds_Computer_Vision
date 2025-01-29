import time
import pygame
from GameState import GameState
import Vision


class PlayingState(GameState):
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            self.game.set_state(self.game.level_pause_state)

    def update(self):
        if Vision.pinch_detected:
            if not self.game.mouse_pressed and self.game.level.number_of_birds > 0:
                self.game.resources.play_stretch_sound()
            self.game.mouse_pressed = True
            self.game.x_mouse, self.game.y_mouse = Vision.mouse_x, Vision.mouse_y

        if not Vision.pinch_detected and self.game.mouse_pressed:
            self.game.mouse_pressed = False
            if self.game.level.number_of_birds > 0:
                self.game.resources.play_release_sound()
            if self.game.level.number_of_birds > 0:
                self.game.level.number_of_birds -= 1
                self.game.t1 = time.time() * 1000
                xo = 154
                yo = 156
                if self.game.mouse_distance > self.game.rope_length:
                    self.game.mouse_distance = self.game.rope_length
                if self.game.x_mouse < self.game.sling_x + 10:
                    bird = self.game.bird_factory.create_character(self.game.mouse_distance, self.game.angle, xo, yo,
                                                                   self.game.space, self.game.bird_size)
                    self.game.birds.append(bird)
                else:
                    bird = self.game.bird_factory.create_character(-self.game.mouse_distance, self.game.angle, xo, yo,
                                                                   self.game.space, self.game.bird_size)
                    self.game.birds.append(bird)
                if self.game.level.number_of_birds == 0:
                    self.game.t2 = time.time()

        self.check_level_cleared()
        self.check_level_failed()

    def check_level_cleared(self):
        if self.game.level.number_of_birds >= 0 and len(self.game.pigs) == 0:
            if self.game.bonus_score_once:
                self.game.score += (self.game.level.number_of_birds - 1) * 10000
            self.game.bonus_score_once = False
            self.game.set_state(self.game.level_cleared_state)

    def check_level_failed(self):
        if self.game.level.number_of_birds <= 0 < len(self.game.pigs) and time.time() - self.game.t2 > 6:
            self.game.set_state(self.game.level_failed_state)
