from Size import Size


class SmallSize(Size):

    def get_mass(self) -> float:
        return 4

    def get_radius(self) -> float:
        return 8

    def get_life(self) -> int:
        return 20
