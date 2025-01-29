from Pig import Pig
from Size import Size


class PigFactory:

    @staticmethod
    def create_character(x, y, space, size: Size) -> Pig:
        return Pig(x, y, space, size)
