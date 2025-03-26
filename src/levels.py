import pygame
import random
from player import Sprite
from game_objects import LevelEnd, Platform, Ground, Spike
from config import HEIGHT, WIDTH, GROUND_HEIGHT

class Level:
    def __init__(self, level_number):
        self.platforms = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.level_ends = pygame.sprite.Group()
        self.level_number = level_number

        self.create_level()

    def create_level(self):
        ground = Ground(0, WIDTH * 2)
        self.platforms.add(ground)

        if self.level_number == 1:
            self.create_level_one()

    def create_level_one(self):
        x = 200
        y = 200
        for i in range(4):
            platform = Platform(x, HEIGHT - GROUND_HEIGHT - y, 200)
            self.platforms.add(platform)

            if i != 0 and i != 3:
                spike = Spike(platform.rect.centerx - 15, platform.rect.centery - 30)
                self.spikes.add(spike)

            if i == 3:
                level_end = LevelEnd(x + 70, HEIGHT - GROUND_HEIGHT - y - 80)
                self.level_ends.add(level_end)

            x += 500 + random.randint(0, 100)
            y += 100 + random.randint(0, 100)

        x = 0
        y = GROUND_HEIGHT

        for i in range(round((WIDTH / 30))):
            spike = Spike(x,  HEIGHT - GROUND_HEIGHT - y + 20)
            self.spikes.add(spike)
            x+=30

    def draw(self, screen):
        self.platforms.draw(screen)
        self.spikes.draw(screen)
        self.level_ends.draw(screen)

    def update(self):
        self.platforms.update()
        self.spikes.update()
        self.level_ends.update()
