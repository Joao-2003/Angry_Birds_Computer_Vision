from Polygon import Polygon
from PigFactory import PigFactory
from SmallSize import SmallSize
from NormalSize import NormalSize
from BigSize import BigSize
import random


class Level:

    def __init__(self, game, pigs, columns, beams, space, birds, pig_size):
        self.game = game
        self.pigs = pigs
        self.columns = columns
        self.beams = beams
        self.space = space
        self.birds = birds
        self.number = 0
        self.number_of_birds = 4
        self.pig_factory = PigFactory()
        self.pig_size = pig_size

    def open_flat(self, x, y, n):
        """Create an open flat structure"""
        y0 = y
        for i in range(n):
            y = y0+100+i*100
            p = (x, y)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+60, y)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+30, y+50)
            self.beams.append(Polygon(p, 85, 20, self.space))

    def closed_flat(self, x, y, n):
        """Create a closed flat structure"""
        y0 = y
        for i in range(n):
            y = y0+100+i*125
            p = (x+1, y+22)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+60, y+22)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+30, y+70)
            self.beams.append(Polygon(p, 85, 20, self.space))
            p = (x+30, y-30)
            self.beams.append(Polygon(p, 85, 20, self.space))

    def horizontal_pile(self, x, y, n):
        """Create a horizontal pile"""
        y += 70
        for i in range(n):
            p = (x, y+i*20)
            self.beams.append(Polygon(p, 85, 20, self.space))

    def vertical_pile(self, x, y, n):
        """Create a vertical pile"""
        y += 10
        for i in range(n):
            p = (x, y+85+i*85)
            self.columns.append(Polygon(p, 20, 85, self.space))

    def build_0(self):
        """level 0"""
        pig1 = self.pig_factory.create_character(980, 100, self.space, self.pig_size)
        self.pigs.append(pig1)
        self.number_of_birds = 5
        if self.game.bool_space:
            self.number_of_birds = 8

    def build_1(self):
        """level 1"""
        pig1 = self.pig_factory.create_character(980, 100, self.space, self.pig_size)
        self.pigs.append(pig1)
        p = (968, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (992, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        self.number_of_birds = 4
        if self.game.bool_space:
            self.number_of_birds = 8

    def build_2(self):
        """level 2"""
        pig1 = self.pig_factory.create_character(980, 100, self.space, self.pig_size)
        pig2 = self.pig_factory.create_character(985, 182, self.space, self.pig_size)
        self.pigs.append(pig1)
        self.pigs.append(pig2)
        p = (950, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1010, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (980, 150)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (950, 200)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1010, 200)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (980, 240)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4
        if self.game.bool_space:
            self.number_of_birds = 8

    def build_3(self):
        """level 3"""
        pig = self.pig_factory.create_character(1000, 100, self.space, self.pig_size)
        self.pigs.append(pig)
        p = (900, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (850, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (850, 150)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1050, 150)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1105, 210)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4
        if self.game.bool_space:
            self.number_of_birds = 8

    def build_4(self):
        """level 4"""
        pig1 = self.pig_factory.create_character(880, 180, self.space, self.pig_size)
        self.pigs.append(pig1)
        pig2 = self.pig_factory.create_character(1000, 230, self.space, self.pig_size)
        self.pigs.append(pig2)
        p = (880, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (880, 150)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (1000, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1000, 180)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1000, 210)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4
        if self.game.bool_space:
            self.number_of_birds = 8

    def build_5(self):
        """level 5"""
        pig = self.pig_factory.create_character(950, 320, self.space, self.pig_size)
        pig.life = 25
        self.pigs.append(pig)
        pig = self.pig_factory.create_character(885, 225, self.space, self.pig_size)
        pig.life = 25
        self.pigs.append(pig)
        pig = self.pig_factory.create_character(1005, 225, self.space, self.pig_size)
        pig.life = 25
        self.pigs.append(pig)
        p = (1100, 100)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1070, 152)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (1040, 100)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (980, 100)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (920, 100)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (950, 152)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (1010, 180)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (860, 100)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (800, 100)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (830, 152)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (890, 180)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (860, 223)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (920, 223)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (980, 223)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1040, 223)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (890, 280)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (1010, 280)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (950, 300)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (920, 350)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (980, 350)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (950, 400)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4
        if self.game.bool_space:
            self.number_of_birds = 8

    def build_6(self):
        """level 6"""
        pig = self.pig_factory.create_character(900, 300, self.space, self.pig_size)
        self.pigs.append(pig)
        pig = self.pig_factory.create_character(1000, 500, self.space, self.pig_size)
        self.pigs.append(pig)
        pig = self.pig_factory.create_character(1100, 400, self.space, self.pig_size)
        self.pigs.append(pig)
        self.number_of_birds = 4
        if self.game.bool_space:
            self.number_of_birds = 8

    def build_7(self):
        """level 7"""
        pig = self.pig_factory.create_character(900, 70, self.space, self.pig_size)
        self.pigs.append(pig)
        pig = self.pig_factory.create_character(1000, 152, self.space, self.pig_size)
        self.pigs.append(pig)
        for i in range(9):
            p = (800, 70 + i * 21)
            self.beams.append(Polygon(p, 85, 20, self.space))
        for i in range(4):
            p = (1000, 70 + i * 21)
            self.beams.append(Polygon(p, 85, 20, self.space))
        p = (970, 176)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1026, 176)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1000, 230)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4
        if self.game.bool_space:
            self.number_of_birds = 8

    def build_8(self):
        """level 8"""
        pig = self.pig_factory.create_character(920, 533, self.space, self.pig_size)
        pig.life = 40
        self.pigs.append(pig)
        pig = self.pig_factory.create_character(820, 533, self.space, self.pig_size)
        self.pigs.append(pig)
        pig = self.pig_factory.create_character(720, 633, self.space, self.pig_size)
        self.pigs.append(pig)
        self.closed_flat(895, 423, 1)
        self.vertical_pile(900, 0, 5)
        self.vertical_pile(926, 0, 5)
        self.vertical_pile(950, 0, 5)
        self.number_of_birds = 4
        if self.game.bool_space:
            self.number_of_birds = 8

    def build_9(self):
        """level 9"""
        pig = self.pig_factory.create_character(978, 180, self.space, self.pig_size)
        pig.life = 30
        self.pigs.append(pig)
        pig = self.pig_factory.create_character(978, 280, self.space, self.pig_size)
        pig.life = 30
        self.pigs.append(pig)
        pig = self.pig_factory.create_character(978, 80, self.space, self.pig_size)
        pig.life = 30
        self.pigs.append(pig)
        self.open_flat(950, 0, 3)
        self.vertical_pile(850, 0, 3)
        self.vertical_pile(830, 0, 3)
        self.number_of_birds = 4
        if self.game.bool_space:
            self.number_of_birds = 8

    def build_10(self):
        """level 10"""
        pig = self.pig_factory.create_character(1000, 180, self.space, self.pig_size)
        pig.life = 30
        self.pigs.append(pig)
        pig = self.pig_factory.create_character(1078, 280, self.space, self.pig_size)
        pig.life = 30
        self.pigs.append(pig)
        pig = self.pig_factory.create_character(900, 80, self.space, self.pig_size)
        pig.life = 30
        self.pigs.append(pig)
        self.open_flat(1050, 0, 3)
        self.open_flat(963, 0, 2)
        self.open_flat(880, 0, 1)
        self.number_of_birds = 4
        if self.game.bool_space:
            self.number_of_birds = 8

    def build_11(self):
        """level 11"""
        pig = self.pig_factory.create_character(1000, 180, self.space, self.pig_size)
        pig.life = 20
        self.pigs.append(pig)
        pig = self.pig_factory.create_character(900, 180, self.space, self.pig_size)
        pig.life = 20
        self.pigs.append(pig)
        self.open_flat(1050, 0, 3)
        self.open_flat(963, 0, 2)
        self.open_flat(880, 0, 2)
        self.open_flat(790, 0, 3)
        self.number_of_birds = 4
        if self.game.bool_space:
            self.number_of_birds = 8

    def build_12(self):
        """level 12"""
        pig = self.pig_factory.create_character(960, 250, self.space, self.pig_size)
        pig.life = 20
        self.pigs.append(pig)
        pig = self.pig_factory.create_character(820, 160, self.space, self.pig_size)
        self.pigs.append(pig)
        pig = self.pig_factory.create_character(1100, 160, self.space, self.pig_size)
        self.pigs.append(pig)
        self.vertical_pile(900, 0, 3)
        self.vertical_pile(930, 0, 3)
        self.vertical_pile(1000, 0, 3)
        self.vertical_pile(1030, 0, 3)
        self.horizontal_pile(970, 250, 2)
        self.horizontal_pile(820, 0, 4)
        self.horizontal_pile(1100, 0, 4)
        self.number_of_birds = 4
        if self.game.bool_space:
            self.number_of_birds = 8

    def build_13(self):
        """level 13"""
        pig = self.pig_factory.create_character(820, 177, self.space, self.pig_size)
        self.pigs.append(pig)
        pig = self.pig_factory.create_character(960, 150, self.space, self.pig_size)
        self.pigs.append(pig)
        pig = self.pig_factory.create_character(1100, 130, self.space, self.pig_size)
        self.pigs.append(pig)
        pig = self.pig_factory.create_character(890, 270, self.space, self.pig_size)
        pig.life = 30
        self.pigs.append(pig)
        self.horizontal_pile(800, 0, 5)
        self.horizontal_pile(950, 0, 3)
        self.horizontal_pile(1100, 0, 2)
        self.vertical_pile(745, 0, 2)
        self.vertical_pile(855, 0, 2)
        self.vertical_pile(900, 0, 2)
        self.vertical_pile(1000, 0, 2)
        p = (875, 230)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4
        if self.game.bool_space:
            self.number_of_birds = 8

    def restart(self):
        """Delete all objects of the level"""
        pigs_to_remove = []
        birds_to_remove = []
        columns_to_remove = []
        beams_to_remove = []
        for pig in self.pigs:
            pigs_to_remove.append(pig)
        for pig in pigs_to_remove:
            self.space.remove(pig.shape, pig.shape.body)
            self.pigs.remove(pig)
        for bird in self.birds:
            birds_to_remove.append(bird)
        for bird in birds_to_remove:
            self.space.remove(bird.shape, bird.shape.body)
            self.birds.remove(bird)
        for column in self.columns:
            columns_to_remove.append(column)
        for column in columns_to_remove:
            self.space.remove(column.shape, column.shape.body)
            self.columns.remove(column)
        for beam in self.beams:
            beams_to_remove.append(beam)
        for beam in beams_to_remove:
            self.space.remove(beam.shape, beam.shape.body)
            self.beams.remove(beam)

    def load_level(self, number=0):
        """Load the level"""
        self.number = number
        if self.number > 13:
            self.load_special_level()
        else:
            self.load_level_data()

    def load_level_data(self):
        build_name = 'build_' + str(self.number)
        getattr(self, build_name)()

    def load_special_level(self):
        level1_number = random.randint(0, 13)
        level2_number = random.randint(0, 13)
        types = [SmallSize(), NormalSize(), BigSize()]
        self.pig_size = random.choice(types)
        level1 = Level(self.game, [], [], [], self.space, [], self.pig_size)
        level1.load_level(level1_number)
        self.pig_size = random.choice(types)
        level2 = Level(self.game, [], [], [], self.space, [], self.pig_size)
        level2.load_level(level2_number)
        self.combine_with(level1)
        self.combine_with_shifted(level2)
        self.number_of_birds = random.randint(5, 8)
        self.game.bird_size = random.choice(types)

    def combine_with(self, other_level):
        self.pigs += other_level.pigs
        self.columns += other_level.columns
        self.beams += other_level.beams

    def combine_with_shifted(self, other_level):
        self.pigs += [self.shift_element(pig, -450) for pig in other_level.pigs]
        self.columns += [self.shift_element(column, -450) for column in other_level.columns]
        self.beams += [self.shift_element(beam, -450) for beam in other_level.beams]

    @staticmethod
    def shift_element(element: 'Polygon', shift_x: int) -> 'Polygon':
        position = element.shape.body.position
        element.shape.body.position = (position[0] + shift_x, position[1])
        return element
