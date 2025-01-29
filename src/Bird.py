from pymunk import Vec2d
from Character import Character
from Size import Size


class Bird(Character):

    def __init__(self, distance, angle, x, y, space, size: Size):
        collision_type = 0
        super().__init__(x, y, space, size, collision_type)
        power = distance * 53
        impulse = power * Vec2d(1, 0)
        self.body.apply_impulse_at_local_point(impulse.rotated(-angle))
