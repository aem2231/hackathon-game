from .base_level import BaseLevel
from game_objects import Platform, Spike, LevelEnd
from config import Physics, Display, Scale, SpikeCfg, Images

class Level4(BaseLevel):
    def __init__(self):
        super().__init__()
        self.spawn_x = Scale.scale_x(200)  # Player spawn position
        self.spawn_y = Scale.scale_y(750)
        self.create_level()

    def create_level(self):
        # Creates spawn platform
        spawn_width = Scale.scale_x(300)
        spawn_x = Scale.scale_x(100)
        spawn_y = Scale.scale_y(800)

        spawn_platform = Platform(
            x=spawn_x, 
            y=spawn_y,
            width=spawn_width
            )
        self.platforms.add(spawn_platform)

        # Creates spikes
        ground_spike = Spike(
            x=0,
            y=Display.HEIGHT - Physics.GROUND_HEIGHT - 1,
            width=Scale.scale_x(5000),
            height=Scale.scale_y(SpikeCfg.DEFAULT_HEIGHT)
            )
        self.spikes.add(ground_spike)


        # Creates the level end & associated platform
        end_width = Scale.scale_x(200)
        end_x = Scale.scale_x(1800)
        end_y = Scale.scale_y(650)

        end_platform = Platform(
            x=end_x, 
            y=end_y,
            width=end_width
            )
        self.platforms.add(end_platform)

        level_end = LevelEnd(
                x=end_platform.rect.centerx - Images.level_end["WIDTH"] / 2,
                y=end_y - Images.level_end["HEIGHT"] / 2,
            )
        self.level_ends.add(level_end)
