import pygame
import pymunk as pm
from Level import Level
import Vision
import threading
from Physics import Physics
from Render import Renderer
from BirdFactory import BirdFactory
from PigFactory import PigFactory
from Subject import Subject
from PlayingState import PlayingState
from LevelClearedState import LevelClearedState
from LevelFailedState import LevelFailedState
from LevelPausedState import LevelPausedState
from SmallSize import SmallSize
from NormalSize import NormalSize
from BigSize import BigSize


class Resources:

    def __init__(self, game):
        self.game = game

    @staticmethod
    def load_music():
        """Load the music"""
        song1 = '../resources/sounds/angry-birds.ogg'
        pygame.mixer.music.load(song1)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    def load_sounds(self):
        """Load the sound effects"""
        self.stretch_sound = pygame.mixer.Sound('../resources/sounds/stretch.ogg')
        self.release_sound = pygame.mixer.Sound('../resources/sounds/release.ogg')
        self.pig_sound = pygame.mixer.Sound('../resources/sounds/pig.ogg')

    def play_stretch_sound(self):
        self.stretch_sound.play()

    def play_release_sound(self):
        self.release_sound.play()

    def play_pig_sound(self):
        self.pig_sound.play()

    def init(self):
        self.game.vision_thread = threading.Thread(target=Vision.detect_hand_movements)
        self.game.vision_thread.start()
        self.game.subject = Subject()
        pygame.init()
        self.game.screen = pygame.display.set_mode((1200, 650))
        self.game.redbird = pygame.image.load('../resources/images/red-bird3.png').convert_alpha()
        self.game.background2 = pygame.image.load('../resources/images/background3.png').convert_alpha()
        self.game.sling_image = pygame.image.load('../resources/images/sling-3.png').convert_alpha()
        self.game.full_sprite = pygame.image.load('../resources/images/full-sprite.png').convert_alpha()
        rect = pygame.Rect(181, 1050, 50, 50)
        cropped = self.game.full_sprite.subsurface(rect).copy()
        self.game.pig_image = pygame.transform.scale(cropped, (30, 30))
        self.game.buttons = pygame.image.load('../resources/images/selected-buttons.png').convert_alpha()
        self.game.pig_happy = pygame.image.load('../resources/images/pig_failed.png').convert_alpha()
        self.game.stars = pygame.image.load('../resources/images/stars-edited.png').convert_alpha()
        rect = pygame.Rect(0, 0, 200, 200)
        self.game.star1 = self.game.stars.subsurface(rect).copy()
        rect = pygame.Rect(204, 0, 200, 200)
        self.game.star2 = self.game.stars.subsurface(rect).copy()
        rect = pygame.Rect(426, 0, 200, 200)
        self.game.star3 = self.game.stars.subsurface(rect).copy()
        self.game.one_star = 20000
        self.game.two_star = 40000
        self.game.three_star = 60000
        rect = pygame.Rect(164, 10, 60, 60)
        self.game.pause_button = self.game.buttons.subsurface(rect).copy()
        rect = pygame.Rect(24, 4, 100, 100)
        self.game.replay_button = self.game.buttons.subsurface(rect).copy()
        rect = pygame.Rect(142, 365, 130, 100)
        self.game.next_button = self.game.buttons.subsurface(rect).copy()
        self.game.clock = pygame.time.Clock()
        rect = pygame.Rect(18, 212, 100, 100)
        self.game.play_button = self.game.buttons.subsurface(rect).copy()
        self.game.running = True
        self.game.space = pm.Space()
        self.game.space.gravity = (0.0, -700.0)
        self.game.pigs = []
        self.game.birds = []
        self.game.balls = []
        self.game.polys = []
        self.game.beams = []
        self.game.columns = []
        self.game.poly_points = []
        self.game.ball_number = 0
        self.game.polys_dict = {}
        self.game.mouse_distance = 0
        self.game.rope_length = 90
        self.game.angle = 0
        self.game.x_mouse = 0
        self.game.y_mouse = 0
        self.game.count = 0
        self.game.mouse_pressed = False
        self.game.t1 = 0
        self.game.tick_to_next_circle = 10
        self.game.RED = (255, 0, 0)
        self.game.BLUE = (0, 0, 255)
        self.game.BLACK = (0, 0, 0)
        self.game.WHITE = (255, 255, 255)
        self.game.sling_x, self.game.sling_y = (135, 450)
        self.game.sling2_x, self.game.sling2_y = (160, 450)
        self.game.score = 0
        self.game.game_state = 0
        self.game.bird_path = []
        self.game.counter = 0
        self.game.restart_counter = False
        self.game.bonus_score_once = True
        self.game.bold_font = pygame.font.SysFont('arial', 30, bold=True)
        self.game.bold_font2 = pygame.font.SysFont('arial', 40, bold=True)
        self.game.bold_font3 = pygame.font.SysFont('arial', 50, bold=True)
        self.game.wall = False
        self.game.bool_space = False
        self.game.mouse_clicked = False
        self.game.static_body = pm.Body(body_type=pm.Body.STATIC)
        self.game.static_lines = [pm.Segment(self.game.static_body, (0.0, 60.0), (1200.0, 60.0), 0.0)]
        self.game.static_lines1 = [pm.Segment(self.game.static_body, (1200.0, 60.0), (1200.0, 800.0), 0.0)]
        for line in self.game.static_lines:
            line.elasticity = 0.95
            line.friction = 1
            line.collision_type = 3
        for line in self.game.static_lines1:
            line.elasticity = 0.95
            line.friction = 1
            line.collision_type = 3
        self.game.space.add(self.game.static_body)
        for line in self.game.static_lines:
            self.game.space.add(line)
        self.load_music()
        self.load_sounds()
        self.game.physics = Physics(self.game)
        self.game.physics.setup_collision_handlers()
        self.game.renderer = Renderer(self.game)
        self.game.bird_factory = BirdFactory()
        self.game.pig_factory = PigFactory()
        self.game.playing_state = PlayingState(self.game)
        self.game.level_cleared_state = LevelClearedState(self.game)
        self.game.level_failed_state = LevelFailedState(self.game)
        self.game.level_pause_state = LevelPausedState(self.game)
        self.game.state = self.game.playing_state
        self.game.bird_size = NormalSize()
        self.game.pig_size = BigSize()
        self.game.level = Level(self.game, self.game.pigs, self.game.columns, self.game.beams, self.game.space,
                                self.game.birds, self.game.pig_size)
        self.game.level.load_level()

        