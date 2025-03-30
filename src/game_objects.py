import pygame
from config import Physics, Colours, Display, Scale

# The classes in the file are game objects, refer to docstrings on how to use them

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, width):
        """
        Creates a ground object at a specific horizontal position with a given width.

        The ground is positioned at the bottom of the screen and uses the configured ground height.

        Parameters:
            x (int): The x-coordinate of the ground's starting position.
            width (int): The width of the ground.
        """
        super().__init__()
        self.image = pygame.Surface((width, Physics.GROUND_HEIGHT))
        self.image.fill(Colours.SURFACE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = round(Display.HEIGHT - Physics.GROUND_HEIGHT)

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        """
        Creates a platform object at a specific position with a given width.

        Platforms are elevated surfaces that can be used as obstacles or paths.

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
        Creates a vertical wall object at a specific position with a given height.

        Walls act as vertical barriers in the game world.

        Parameters:
            x (int): The x-coordinate of the wall's position.
            y (int): The y-coordinate of the wall's position.
            height (int): The height of the wall.
        """
        super().__init__()
        self.image = pygame.Surface((Physics.GROUND_HEIGHT // 2, height))
        self.image.fill(Colours.PLATFORM)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        """
        Creates a spike object at a specific position with a given width and height.

        Spikes are obstacles that can harm the player.

        Parameters:
            x (int): The x-coordinate of the spike's position.
            y (int): The y-coordinate of the spike's position.
            width (int): The width of the spike.
            height (int): The height of the spike.
        """
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(Colours.RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class LevelEnd(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        Creates a level end object at a specific position.

        The level end is a goal object that players must reach to complete the level.

        Parameters:
            x (int): The x-coordinate of the level end's position.
            y (int): The y-coordinate of the level end's position.
        """
        super().__init__()
        self.image = pygame.image.load("./assets/img/end.png").convert_alpha()
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        self.scaled_width = Scale.scale_x(self.image_width)
        self.scaled_height = Scale.scale_y(self.image_height)
        self.image = pygame.transform.scale(self.image, (self.scaled_width, self.scaled_height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        """
        Creates a block object at a specific position with a given width and height.

        Blocks are rectangular objects that can serve as obstacles or platforms.

        Parameters:
            x (int): The x-coordinate of the block's position.
            y (int): The y-coordinate of the block's position.
            width (int): The width of the block.
            height (int): The height of the block.
        """
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(Colours.PLATFORM)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class WorldBoundaries(pygame.sprite.Sprite):
    def __init__(self):
        """
        Creates invisible boundaries around the edges of the screen.

        These boundaries prevent the player or other objects from leaving the game world.
        """
        super().__init__()

        # Left boundary
        self.left_wall = Wall(0, 0, Display.HEIGHT)

        # Right boundary
        self.right_wall = Wall(Display.WIDTH - Physics.GROUND_HEIGHT // 2, 0, Display.HEIGHT)

        # Top boundary
        self.top_wall = Platform(0, 0, Display.WIDTH)
