import pymunk as pm
from pymunk import Vec2d
import pygame


class Polygon:

    def __init__(self, pos, length, height, space, mass=5.0):
        moment = 1000
        body = pm.Body(mass, moment)
        body.position = Vec2d(*pos)
        shape = pm.Poly.create_box(body, (length, height))
        shape.color = (0, 0, 255)
        shape.friction = 0.5
        shape.collision_type = 2
        space.add(body, shape)
        self.body = body
        self.shape = shape
        wood = pygame.image.load('../resources/images/wood.png').convert_alpha()
        wood2 = pygame.image.load('../resources/images/wood2.png').convert_alpha()
        rect = pygame.Rect(251, 357, 86, 22)
        self.beam_image = wood.subsurface(rect).copy()
        rect = pygame.Rect(16, 252, 22, 84)
        self.column_image = wood2.subsurface(rect).copy()
