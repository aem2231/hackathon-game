import pygame
from game_objects import Ground, WorldBoundaries
from config import Display, Physics, Scale

class BaseLevel:
    def __init__(self):
        # Initialize game object groups
        self.platforms = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.level_ends = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        # Create world boundaries
        boundaries = WorldBoundaries()
        self.walls.add(boundaries.left_wall)
        self.walls.add(boundaries.right_wall)

        # Default spawn coordinates
        self.spawn_x = Scale.scale_x(200)
        self.spawn_y = Display.HEIGHT - Physics.GROUND_HEIGHT - Scale.scale_y(800)

        ground = Ground(0, Display.WIDTH * 2)
        self.platforms.add(ground)

    def draw(self, screen):
        self.platforms.draw(screen)
        self.spikes.draw(screen)
        self.level_ends.draw(screen)
        self.walls.draw(screen)

    def update(self):
        self.platforms.update()
        self.spikes.update()
        self.level_ends.update()
        self.walls.update()
