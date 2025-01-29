import pymunk as pm
from Size import Size
from abc import ABC, abstractmethod


class Character(ABC):

    @abstractmethod
    def __init__(self, x, y, space, size: Size, collision_type: int):
        self.life = size.get_life()
        mass = size.get_mass()
        radius = size.get_radius()
        inertia = pm.moment_for_circle(mass, 0, radius, (0, 0))
        body = pm.Body(mass, inertia)
        body.position = (x, y)
        shape = pm.Circle(body, radius, (0, 0))
        shape.elasticity = 0.95
        shape.friction = 1
        shape.collision_type = collision_type
        space.add(body, shape)
        self.body = body
        self.shape = shape
