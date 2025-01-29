from Bird import Bird
from Size import Size


class BirdFactory:

    @staticmethod
    def create_character(distance, angle, x, y, space, size: Size) -> Bird:
        return Bird(distance, angle, x, y, space, size)
