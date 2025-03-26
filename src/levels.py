import pygame
import random
from game_objects import LevelEnd, Platform, Ground, Spike
from config import Physics, Display


class Level:
    def __init__(self, level_number):
        self.platforms = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.level_ends = pygame.sprite.Group()
        self.level_number = level_number

        self.create_level()

    def create_level(self):
        ground = Ground(0, Display.WIDTH * 2)
        self.platforms.add(ground)

        if self.level_number == 1:
            self.create_level_one()
        else:
            self.create_level_two()

    # This function defines a level. It can somewhat serve as a template for other levels
    def create_level_one(self):
        x = 200
        y = 200

        for i in range(4):
            platform = Platform(x, Display.HEIGHT - Physics.GROUND_HEIGHT - y, 200)
            self.platforms.add(platform)

            if i != 0 and i != 3:
                spike = Spike(platform.rect.centerx - 15, platform.rect.centery - 30)
                self.spikes.add(spike)

            if i == 3:
                level_end = LevelEnd(x + 70, Display.HEIGHT - Physics.GROUND_HEIGHT - y - 80)
                self.level_ends.add(level_end) # Every level needs to have a level end, otherwise you will be stuck there.

            x += 500 + random.randint(0, 50)
            y += 100 + random.randint(0, 50)

        x = 0
        y = Physics.GROUND_HEIGHT

        for i in range(round((Display.WIDTH / 30))):
            spike = Spike(x,  Display.HEIGHT - Physics.GROUND_HEIGHT - y + 20)
            self.spikes.add(spike)
            x+=30

    def create_level_two(self):
        x, y  = 200, 200

        for i in range(4):
            platform = Platform(x, Display.HEIGHT - Physics.GROUND_HEIGHT - y, 200)
            self.platforms.add(platform)
            y += 200

        platform = Platform(x, Display.HEIGHT - Physics.GROUND_HEIGHT - y, 800)
        self.platforms.add(platform)

        for i in range(4):
            spike = Spike(x+300, Display.HEIGHT - Physics.GROUND_HEIGHT - y - 30)
            self.spikes.add(spike)
            y+=30

        x, y = 1250, 1000
        y -= 300

        for i in range(3):
            platform = Platform(x, Display.HEIGHT - Physics.GROUND_HEIGHT - y, 150)
            self.platforms.add(platform)

            spike = Spike(x-30, Display.HEIGHT - Physics.GROUND_HEIGHT - y - 5)
            self.spikes.add(spike)

            spike = Spike(x+120, Display.HEIGHT - Physics.GROUND_HEIGHT - y - 5)
            self.spikes.add(spike)

            y-=100
            x+=500

        x = Display.WIDTH - 300
        y = Display.HEIGHT - 150

        platform = Platform(x, y, 200)
        self.platforms.add(platform)

        level_end = LevelEnd(x + 70, y - 100)
        self.level_ends.add(level_end)

        x = 0
        y = Physics.GROUND_HEIGHT

        for i in range(round((Display.WIDTH / 30))):
            spike = Spike(x,  Display.HEIGHT - Physics.GROUND_HEIGHT - y + 20)
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
