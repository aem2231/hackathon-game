import pygame
from config import *

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, width):
        super().__init__()
        self.image = pygame.Surface((width, GROUND_HEIGHT))
        self.image.fill(GROUND_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = HEIGHT - GROUND_HEIGHT

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        """
        Creates a platform at a specific position (x, y) with a given width.

        Parameters:
        x (int): The x-coordinate of the platform's position.
        y (int): The y-coordinate of the platform's position.
        width (int): The width of the platform.
        """
        super().__init__()
        self.image = pygame.Surface((width, GROUND_HEIGHT // 2))
        self.image.fill(PLATFORM_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
