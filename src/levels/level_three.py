from .base_level import BaseLevel
from game_objects import Platform, Spike, LevelEnd, Wall
from config import Physics, Display, Scale, SpikeCfg, Player

class Level3(BaseLevel):
    def __init__(self):
        super().__init__()
        self.spawn_x = Scale.scale(200)
        self.spawn_y = Display.HEIGHT - Physics.GROUND_HEIGHT - Player.HEIGHT
        self.create_level()

    def create_level(self):
        spike = Spike(
            x = Scale.scale_x(200),
            y = Display.HEIGHT - Physics.GROUND_HEIGHT - Player.HEIGHT * 1.5,
            width = Scale.scale_x(1100),
            height = SpikeCfg.DEFAULT_HEIGHT
        )
        self.spikes.add(spike)

        spike = Spike(
            x = Scale.scale_x(100),
            y = Display.HEIGHT - Physics.GROUND_HEIGHT - Player.HEIGHT * 2,
            width = Scale.scale_x(1220),
            height = SpikeCfg.DEFAULT_HEIGHT
        )
        self.spikes.add(spike)

        wall_height = Scale.scale_y(750)
        wall_y = Display.HEIGHT - Physics.GROUND_HEIGHT - wall_height

        wall = Wall(
            x = Scale.scale_x(1250),
            y = wall_y,
            height = wall_height
        )
        self.walls.add(wall)

        wall = Wall(
            x = Scale.scale_x(100),
            y = wall_y,
            height = wall_height
        )
        self.walls.add(wall)

        platform = Platform(
            x = Scale.scale_x(1210),
            y = Display.HEIGHT - Physics.GROUND_HEIGHT -Scale.scale(300),
            width = Player.BASE_WIDTH
        )
        self.platforms.add(platform)

        platform = Platform(
            x = Scale.scale_x(900),
            y = Display.HEIGHT - Physics.GROUND_HEIGHT -Scale.scale_y(250),
            width = Player.BASE_WIDTH
        )
        self.platforms.add(platform)
