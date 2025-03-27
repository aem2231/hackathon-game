from .base_level import BaseLevel
from game_objects import Platform, Spike, LevelEnd
from config import Physics, Display, Scale, SpikeCfg

class Level2(BaseLevel):
    def __init__(self):
        super().__init__()
        self.create_level()

    def create_level(self):
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

        x = Scale.scale(2500)
        y = Scale.scale(1700)

        platform = Platform(x, y, 200)
        self.platforms.add(platform)

        level_end = LevelEnd(x + Scale.scale(80), y - Scale.scale(110))
        self.level_ends.add(level_end)

        x = 0
        y = Scale.scale(Physics.GROUND_HEIGHT)

        spike = Spike(x, Display.HEIGHT - Physics.GROUND_HEIGHT - y + 20, 5000, SpikeCfg.DEFAULT_HEIGHT)
        self.spikes.add(spike)
