from Size import Size


class NormalSize(Size):

    def get_mass(self) -> float:
        return 5

    def get_radius(self) -> float:
        return 14

    def get_life(self) -> int:
        return 25