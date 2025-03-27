import pygame
import random
from game_objects import LevelEnd, Platform, Ground, Spike
from config import Physics, Display, Scale, SpikeCfg
from telnetlib import WILL


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
        x = Scale.scale(150)
        y = Scale.scale(200)  # coordinates should be scaled using Scale.scale(n)

        for i in range(4):
            platform = Platform(x, Display.HEIGHT - Physics.GROUND_HEIGHT - y, 200)
            self.platforms.add(platform)

            if i != 0 and i != 3:
                spike = Spike(platform.rect.centerx - 15, platform.rect.centery - 30, SpikeCfg.DEFAULT_WIDTH, SpikeCfg.DEFAULT_HEIGHT)
                self.spikes.add(spike)

            if i == 3:
                level_end = LevelEnd( x + Scale.scale(120), Display.HEIGHT - Physics.GROUND_HEIGHT - y - Scale.scale(110))
                self.level_ends.add(level_end) # Every level needs to have a level end, otherwise you will be stuck there.

            x += Scale.scale(800 + random.randint(0, 50))
            y += Scale.scale(100 + random.randint(0, 50))

        x = 0
        y = Scale.scale(Physics.GROUND_HEIGHT)

        spike = Spike(x, Display.HEIGHT - Physics.GROUND_HEIGHT - y + 20, 5000, SpikeCfg.DEFAULT_HEIGHT)
        self.spikes.add(spike)


    def create_level_two(self):
        x, y  = Scale.scale(200), Scale.scale(200)

        for i in range(4):
            platform = Platform(x, Display.HEIGHT - Physics.GROUND_HEIGHT - y, Scale.scale(200))
            self.platforms.add(platform)
            y += Scale.scale(300)

        platform = Platform(x, Display.HEIGHT - Physics.GROUND_HEIGHT - y, Scale.scale(800))
        self.platforms.add(platform)

        for i in range(4):
            spike = Spike(x+300, Display.HEIGHT - Physics.GROUND_HEIGHT - y - 30, SpikeCfg.DEFAULT_WIDTH, SpikeCfg.DEFAULT_HEIGHT)
            self.spikes.add(spike)
            y+= Scale.scale(30)

        x, y = Scale.scale(1500), Scale.scale(1150)

        for i in range(3):
            platform = Platform(x, Display.HEIGHT - Physics.GROUND_HEIGHT - y, Scale.scale(150))
            self.platforms.add(platform)

            spike = Spike(x-Scale.scale(30), Display.HEIGHT - Physics.GROUND_HEIGHT - y - Scale.scale(5), SpikeCfg.DEFAULT_WIDTH, SpikeCfg.DEFAULT_HEIGHT)
            self.spikes.add(spike)

            spike = Spike(x+Scale.scale(150 + 30), Display.HEIGHT - Physics.GROUND_HEIGHT - y - Scale.scale(5), SpikeCfg.DEFAULT_WIDTH, SpikeCfg.DEFAULT_HEIGHT)
            self.spikes.add(spike)

            y-= Scale.scale(250)
            x+= Scale.scale(450)

        x = Scale.scale(Display.WIDTH - 100)
        y = Scale.scale(Display.HEIGHT - 50)

        platform = Platform(x, y, 200)
        self.platforms.add(platform)

        level_end = LevelEnd(x + 70, y - 100)
        self.level_ends.add(level_end)

        x = 0
        y = Scale.scale(Physics.GROUND_HEIGHT)

        spike = Spike(x, Display.HEIGHT - Physics.GROUND_HEIGHT - y + 20, 5000, SpikeCfg.DEFAULT_HEIGHT)
        self.spikes.add(spike)


    def draw(self, screen):
        self.platforms.draw(screen)
        self.spikes.draw(screen)
        self.level_ends.draw(screen)

    def update(self):
        self.platforms.update()
        self.spikes.update()
        self.level_ends.update()
