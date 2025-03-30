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
        self.image = pygame.Surface((width, Physics.GROUND_HEIGHT // 2))
        self.image.fill(Colours.PLATFORM)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, height):
        """
        Creates a wall at a specific position (x, y) with a given width.

        Parameters:
            x (int): The x-coordinate of the platform's position.
            y (int): The y-coordinate of the platform's position.
        height (int): The width of the platform.
        """
        super().__init__()
        self.image = pygame.Surface((Physics.GROUND_HEIGHT // 2, height))
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
        self.image_height = self.image.get_height()
        self.image_width = self.image.get_width()
        self.scaled_height = Scale.scale_y(self.image_height)
        self.scaled_width = Scale.scale_x(self.image_width)
        self.image_scale  = (self.scaled_height, self.scaled_width)
        self.scaled_image = pygame.transform.scale(self.image, self.image_scale)
        self.rect = self.scaled_image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        """
        Creates a platform at a specific position (x, y) with a given width and height.

        Parameters:
            x (int): The x-coordinate of the block's position.
            y (int): The y-coordinate of the block's position.
            width (int): The width of the platform.
            height (int): The height of the block
        """
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(Colours.PLATFORM)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class WorldBoundaries(pygame.sprite.Sprite):
    def __init__(self):
        """Creates invisible boundaries around the screen edges."""
        super().__init__()

        # Left boundary
        self.left_wall = Wall(0, 0, Display.HEIGHT)

        # Right boundary
        self.right_wall = Wall(Display.WIDTH - Physics.GROUND_HEIGHT // 2, 0, Display.HEIGHT)

        # Top boundary
        self.top_wall = Platform(0, 0, Display.WIDTH)
