import pygame
from Observer import Observer


class WallObserver(Observer):

    def __init__(self, game):
        self.game = game

    def update(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            self.toggle_wall()

    def toggle_wall(self):
        if self.game.wall:
            for line in self.game.static_lines1:
                self.game.space.remove(line)
            self.game.wall = False
        else:
            for line in self.game.static_lines1:
                self.game.space.add(line)
            self.game.wall = True
