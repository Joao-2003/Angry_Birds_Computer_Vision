import pygame
import time
import math
from pymunk import Vec2d


class Renderer:

    def __init__(self, game):
        self.game = game

    @staticmethod
    def to_pygame(p):
        """Convert pymunk to pygame coordinates"""
        return (int(p.x), int(-p.y + 600))

    def render_background(self):
        self.game.screen.fill((130, 200, 100))
        self.game.screen.blit(self.game.background2, (0, -50))

    def render_sling(self):
        rect = pygame.Rect(50, 0, 70, 220)
        self.game.screen.blit(self.game.sling_image, (138, 420), rect)

    def render_sling_action(self):
        if self.game.mouse_pressed and self.game.level.number_of_birds > 0:
            self.game.physics.sling_action()
        elif time.time() * 1000 - self.game.t1 > 300 and self.game.level.number_of_birds > 0:
            self.game.screen.blit(self.game.redbird, (130, 426))
        else:
            pygame.draw.line(self.game.screen, (0, 0, 0), (self.game.sling_x, self.game.sling_y - 8), (self.game.sling2_x, self.game.sling2_y - 7), 5)

    def render_bird_path(self):
        for point in self.game.bird_path:
            pygame.draw.circle(self.game.screen, self.game.WHITE, point, 5, 0)

    def render_waiting_birds(self):
        if self.game.level.number_of_birds > 0:
            for i in range(self.game.level.number_of_birds - 1):
                x = 100 - i * 35
                self.game.screen.blit(self.game.redbird, (x, 508))

    def render_birds(self):
        birds_to_remove = []
        self.game.counter += 1
        for bird in self.game.birds:
            if bird.shape.body.position.y < 0:
                birds_to_remove.append(bird)
            p = self.to_pygame(bird.shape.body.position)
            x, y = p
            x -= 22
            y -= 20
            self.game.screen.blit(self.game.redbird, (x, y))
            pygame.draw.circle(self.game.screen, self.game.BLUE, p, int(bird.shape.radius), 2)
            if self.game.counter >= 3 and time.time() - self.game.t1 < 5:
                self.game.bird_path.append(p)
                self.game.restart_counter = True
        if self.game.restart_counter:
            self.game.counter = 0
            self.game.restart_counter = False
        for bird in birds_to_remove:
            self.game.space.remove(bird.shape, bird.shape.body)
            self.game.birds.remove(bird)

    def render_pigs(self):
        pigs_to_remove = []
        for pig in self.game.pigs:
            if pig.shape.body.position.y < 0:
                pigs_to_remove.append(pig)
            p = self.to_pygame(pig.shape.body.position)
            x, y = p
            angle_degrees = math.degrees(pig.shape.body.angle)
            img = pygame.transform.rotate(self.game.pig_image, angle_degrees)
            w, h = img.get_size()
            x -= w * 0.5
            y -= h * 0.5
            self.game.screen.blit(img, (x, y))
            pygame.draw.circle(self.game.screen, self.game.BLUE, p, int(pig.shape.radius), 2)
        for pig in pigs_to_remove:
            self.game.space.remove(pig.shape, pig.shape.body)
            self.game.pigs.remove(pig)

    def render_static_lines(self):
        for line in self.game.static_lines:
            body = line.body
            pv1 = body.position + line.a.rotated(body.angle)
            pv2 = body.position + line.b.rotated(body.angle)
            p1 = self.to_pygame(pv1)
            p2 = self.to_pygame(pv2)
            pygame.draw.lines(self.game.screen, (150, 150, 150), False, [p1, p2])

    def render_columns_and_beams(self):
        for column in self.game.columns:
            self.draw_poly(column, 'columns', self.game.screen)
        for beam in self.game.beams:
            self.draw_poly(beam, 'beams', self.game.screen)

    def draw_poly(self, polygon, element, screen):
        """Draw beams and columns"""
        poly = polygon.shape
        ps = poly.get_vertices()
        ps.append(ps[0])
        ps = map(self.to_pygame, ps)
        ps = list(ps)
        color = (255, 0, 0)
        pygame.draw.lines(screen, color, False, ps)
        p = poly.body.position
        p = Vec2d(*self.to_pygame(p))
        angle_degrees = math.degrees(poly.body.angle) + 180
        if element == 'beams':
            rotated_logo_img = pygame.transform.rotate(polygon.beam_image, angle_degrees)
        if element == 'columns':
            rotated_logo_img = pygame.transform.rotate(polygon.column_image, angle_degrees)
        offset = Vec2d(*rotated_logo_img.get_size()) / 2.0
        p = p - offset
        np = p
        screen.blit(rotated_logo_img, (np.x, np.y))

    def render_score(self):
        score_font = self.game.bold_font.render('SCORE', 1, self.game.WHITE)
        number_font = self.game.bold_font.render(str(self.game.score), 1, self.game.WHITE)
        self.game.screen.blit(score_font, (1060, 90))
        if self.game.score == 0:
            self.game.screen.blit(number_font, (1100, 130))
        else:
            self.game.screen.blit(number_font, (1060, 130))

    def render_sling_second_part(self):
        rect = pygame.Rect(0, 0, 60, 200)
        self.game.screen.blit(self.game.sling_image, (120, 420), rect)

    def render_level_cleared(self):
        level_cleared = self.game.bold_font3.render('Level Cleared!', 1, self.game.WHITE)
        score_level_cleared = self.game.bold_font2.render(str(self.game.score), 1, self.game.WHITE)
        rect = pygame.Rect(300, 0, 600, 800)
        pygame.draw.rect(self.game.screen, self.game.BLACK, rect)
        self.game.screen.blit(level_cleared, (450, 90))
        if self.game.one_star <= self.game.score <= self.game.two_star:
            self.game.screen.blit(self.game.star1, (310, 190))
        if self.game.two_star <= self.game.score <= self.game.three_star:
            self.game.screen.blit(self.game.star1, (310, 190))
            self.game.screen.blit(self.game.star2, (500, 170))
        if self.game.score >= self.game.three_star:
            self.game.screen.blit(self.game.star1, (310, 190))
            self.game.screen.blit(self.game.star2, (500, 170))
            self.game.screen.blit(self.game.star3, (700, 200))
        self.game.screen.blit(score_level_cleared, (550, 400))
        self.game.screen.blit(self.game.replay_button, (510, 480))
        self.game.screen.blit(self.game.next_button, (620, 480))

    def render_level_failed(self):
        failed = self.game.bold_font3.render('Level Failed', 1, self.game.WHITE)
        rect = pygame.Rect(300, 0, 600, 800)
        pygame.draw.rect(self.game.screen, self.game.BLACK, rect)
        self.game.screen.blit(failed, (450, 90))
        self.game.screen.blit(self.game.pig_happy, (380, 120))
        self.game.screen.blit(self.game.replay_button, (520, 460))

    def render(self):
        self.render_background()
        self.render_sling()
        self.render_sling_action()
        self.render_bird_path()
        self.render_waiting_birds()
        self.render_birds()
        self.render_pigs()
        self.render_static_lines()
        self.render_columns_and_beams()
        self.render_score()
        self.render_sling_second_part()
        if self.game.state == self.game.level_cleared_state:
            self.render_level_cleared()
        elif self.game.state == self.game.level_failed_state:
            self.render_level_failed()
        pygame.display.flip()
