import pygame
from Observer import Observer


class GravityObserver(Observer):

    def __init__(self, game):
        self.game = game

    def update(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            self.toggle_gravity()

    def toggle_gravity(self):
        if self.game.bool_space:
            self.disable_gravity()
        else:
            self.enable_gravity()

    def enable_gravity(self):
        self.game.space.gravity = (0.0, -10.0)
        self.game.bool_space = True

    def disable_gravity(self):
        self.game.space.gravity = (0.0, -700.0)
        self.game.bool_space = False