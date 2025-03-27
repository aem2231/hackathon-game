import pygame
from game_objects import Ground
from config import Display

class BaseLevel:
    def __init__(self):
        self.platforms = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.level_ends = pygame.sprite.Group()

        # Add ground that's common to all levels
        ground = Ground(0, Display.WIDTH * 2)
        self.platforms.add(ground)

    def draw(self, screen):
        self.platforms.draw(screen)
        self.spikes.draw(screen)
        self.level_ends.draw(screen)

    def update(self):
        self.platforms.update()
        self.spikes.update()
        self.level_ends.update()
