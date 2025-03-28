from .base_level import BaseLevel
from game_objects import Platform, Spike, LevelEnd
from config import Physics, Display, Scale, SpikeCfg
import random

class Level1(BaseLevel):
    def __init__(self):
        super().__init__()
        self.spawn_x = Scale.scale_x(200)
        self.spawn_y = Scale.scale_y(200)
        self.create_level()


    def create_level(self):
        x = Scale.scale_x(150)
        y = Scale.scale_y(200)

        for i in range(4):
            platform = Platform(x, Display.HEIGHT - Physics.GROUND_HEIGHT - y, 200)
            self.platforms.add(platform)

            if i != 0 and i != 3:
                spike = Spike(platform.rect.centerx - (SpikeCfg.DEFAULT_WIDTH / 2),
                            platform.rect.centery - SpikeCfg.DEFAULT_HEIGHT,
                            SpikeCfg.DEFAULT_WIDTH,
                            SpikeCfg.DEFAULT_HEIGHT)
                self.spikes.add(spike)

            if i == 3:
                level_end = LevelEnd(x + Scale.scale_x(120),
                                   Display.HEIGHT - Physics.GROUND_HEIGHT - y - Scale.scale_y(60))
                self.level_ends.add(level_end)

            x += Scale.scale_x(450 + random.randint(0, 50))
            y += Scale.scale_y(50 + random.randint(0, 50))

        # Add ground spikes
        spike = Spike(0,
                     Display.HEIGHT - Physics.GROUND_HEIGHT - Scale.scale_y(Physics.GROUND_HEIGHT) + 60,
                     5000,
                     SpikeCfg.DEFAULT_HEIGHT)
        self.spikes.add(spike)
