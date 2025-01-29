import pygame
from Resources import Resources


class Game:

    def __init__(self):
        self.resources = Resources(self)
        self.resources.init()

    def set_state(self, state):
        self.state = state

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    continue
                self.subject.notify_observers(event)
                self.state.handle_input(event)
            self.state.update()
            if self.state == self.level_failed_state or self.level_cleared_state:
                self.x_mouse, self.y_mouse = pygame.mouse.get_pos()
                self.state.update()
            self.physics.update_physics()
            self.renderer.render()
            self.clock.tick(50)
            pygame.display.set_caption('fps: ' + str(self.clock.get_fps()))
        self.vision_thread.join()
        pygame.quit()
