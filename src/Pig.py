from Character import Character
from Size import Size


class Pig(Character):

    def __init__(self, x, y, space, size: Size):
        collision_type = 1
        super().__init__(x, y, space, size, collision_type)
