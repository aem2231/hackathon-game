from .base_level import BaseLevel
from game_objects import Platform, Spike, LevelEnd
from config import Physics, Display, Scale, SpikeCfg, Images
import random

class Level1(BaseLevel):
    def __init__(self):
        super().__init__()
        # Set spawn position using Scale
        self.spawn_x = Scale.scale_x(200)
        self.spawn_y = Scale.scale_y(200)
        self.create_level()

    def create_level(self):
        # Initial platform position
        platform_width = Scale.scale_x(300)
        x = Scale.scale_x(150)
        y = Scale.scale_y(200)

        for i in range(4):
            # Create platform
            platform = Platform(
                x=x,
                y=Display.HEIGHT - Physics.GROUND_HEIGHT - y,
                width=platform_width
            )
            self.platforms.add(platform)

            # Add spikes on middle platforms
            if i != 0 and i != 3:
                spike = Spike(
                    x=platform.rect.centerx - Scale.scale_x(SpikeCfg.DEFAULT_WIDTH / 2),
                    y=platform.rect.bottom - Physics.GROUND_HEIGHT,
                    width=SpikeCfg.DEFAULT_WIDTH,
                    height=SpikeCfg.DEFAULT_HEIGHT
                )
                self.spikes.add(spike)

            # Add level end on last platform
            if i == 3:
                level_end = LevelEnd(
                    x=platform.rect.centerx - Images.level_end["WIDTH"] / 2,
                    y=y
                )
                self.level_ends.add(level_end)

            # Increment positions for next platform
            x += Scale.scale_x(450 + random.randint(0, 50))
            y += Scale.scale_y(50 + random.randint(0, 50))

        # Add ground spikes
        ground_spike = Spike(
            x=0,
            y=Display.HEIGHT - Physics.GROUND_HEIGHT,
            width=Scale.scale_x(5000),
            height=SpikeCfg.DEFAULT_HEIGHT
        )
        self.spikes.add(ground_spike)
