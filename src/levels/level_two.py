from .base_level import BaseLevel
from game_objects import Platform, Spike, LevelEnd
from config import Physics, Display, Scale, SpikeCfg, Player

class Level2(BaseLevel):
    def __init__(self):
        super().__init__()
        self.spawn_x = Scale.scale_x(150)
        self.spawn_y = Display.HEIGHT - Physics.GROUND_HEIGHT - Scale.scale_y(175)
        self.create_level()

    def create_level(self):
        x, y = Scale.scale_x(100), Scale.scale_y(100)

        for i in range(4):
            platform = Platform(x, Display.HEIGHT - Physics.GROUND_HEIGHT - y, Scale.scale_x(175))
            self.platforms.add(platform)
            y += Scale.scale_y(150)

        platform = Platform(x, Display.HEIGHT - Physics.GROUND_HEIGHT - y, Scale.scale_x(500))
        self.platforms.add(platform)

        for i in range(4):
            spike = Spike(x + Scale.scale_x(300),
                        Display.HEIGHT - Physics.GROUND_HEIGHT - y - Scale.scale_y(29),
                        SpikeCfg.DEFAULT_WIDTH,
                        SpikeCfg.DEFAULT_HEIGHT)
            self.spikes.add(spike)
            y += Scale.scale_y(20)

        x, y = Scale.scale_x(900), Scale.scale_y(500)

        for i in range(3):
            platform = Platform(x, Display.HEIGHT - Physics.GROUND_HEIGHT - y, Scale.scale_x(100))
            self.platforms.add(platform)

            spike = Spike(x - Scale.scale_x(30),
                        Display.HEIGHT - Physics.GROUND_HEIGHT - y - Scale.scale_y(5),
                        SpikeCfg.DEFAULT_WIDTH,
                        SpikeCfg.DEFAULT_HEIGHT)
            self.spikes.add(spike)

            spike = Spike(x + Scale.scale_x(130),
                        Display.HEIGHT - Physics.GROUND_HEIGHT - y - Scale.scale_y(5),
                        SpikeCfg.DEFAULT_WIDTH,
                        SpikeCfg.DEFAULT_HEIGHT)
            self.spikes.add(spike)

            y -= Scale.scale_y(50)
            x += Scale.scale_x(350)

        x = Scale.scale_x(1700)
        y = Display.HEIGHT - Physics.GROUND_HEIGHT - Scale.scale_y(100)

        platform = Platform(x, y, Scale.scale_x(150))
        self.platforms.add(platform)

        level_end = LevelEnd(x + Scale.scale_x(80), y - Scale.scale_y(60))
        self.level_ends.add(level_end)

        x = 0
        y = Scale.scale_y(Physics.GROUND_HEIGHT)

        spike = Spike(x,
                     Display.HEIGHT - Physics.GROUND_HEIGHT - y + Scale.scale_y(40),
                     Scale.scale_x(5000),
                     SpikeCfg.DEFAULT_HEIGHT)
        self.spikes.add(spike)
