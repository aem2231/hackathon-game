import pygame
from config import Physics, Colours, Display, Scale

# The classes in the file are game objects, refer to docstrings on how to use them

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, width):
        super().__init__()
        self.image = pygame.Surface((width, Physics.GROUND_HEIGHT))
        self.image.fill(Colours.SURFACE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = round(Display.HEIGHT - Physics.GROUND_HEIGHT)

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
        self.image = pygame.Surface((width * Display.SCALE, Physics.GROUND_HEIGHT // 2))
        self.image.fill(Colours.PLATFORM)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        """Creates a spike at a specific position.

        Paramaters:
            x (int): The x-coordinates of the spikes position.
            y (int): The y-coordinates of the spikes position.
        """

        super().__init__()
        self.image = pygame.Surface((Scale.scale(width), Scale.scale(height)))
        self.image.fill(Colours.RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class LevelEnd(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """Creates a a levvel end at a specific position.

        Paramaters:
            x (int): The x-coordinates of the level end position.
            y (int): The y-coordinates of the level end position.
        """
        super().__init__()
        self.image = pygame.image.load("./assets/img/end.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
