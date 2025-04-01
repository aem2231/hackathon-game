from .base_level import BaseLevel
from game_objects import Platform, Spike, LevelEnd, Wall
from config import Physics, Display, Scale, SpikeCfg, Images
import random

class Level3(BaseLevel):
    def __init__(self):
        super().__init__()
        self.spawn_x = Scale.scale_x(100)
        self.spawn_y = Display.HEIGHT - Physics.GROUND_HEIGHT - Scale.scale_y(250)
        self.create_level()

    def create_level(self):
        platform_width = Scale.scale_x(500)
        x = Scale.scale_x(0)
        y = Scale.scale_y(200)

        # Spawn Platform #
        platform = Platform(
            x=x,
            y=Display.HEIGHT - Physics.GROUND_HEIGHT - y,
            width=platform_width
        )
        self.platforms.add(platform)

        # Above Platform #
        platform_width = Scale.scale_x(3000)
        x = Scale.scale_x(0)
        y = Scale.scale_y(800)

        platform = Platform(
            x=x,
            y=Display.HEIGHT - Physics.GROUND_HEIGHT - y,
            width=platform_width
        )
        self.platforms.add(platform)

        # Death On the bottom #
        ground_spike = Spike(
            x=0,
            y=Display.HEIGHT - Physics.GROUND_HEIGHT - 1,
            width=Scale.scale_x(5000),
            height=Scale.scale_y(SpikeCfg.DEFAULT_HEIGHT)
        )
        self.spikes.add(ground_spike)

        # Platforms of the wall #

        # wall one #
        wall = Wall(x= Scale.scale_x(300), y= Scale.scale_y(230), height= Scale.scale_y(300))
        self.walls.add(wall)
        wall = Wall(x= Scale.scale_x(300), y= Scale.scale_y(490), height= Scale.scale_y(300))
        self.walls.add(wall)

        # wall two #
        wall = Wall(x= Scale.scale_x(500), y= Scale.scale_y(230), height= Scale.scale_y(200))
        self.walls.add(wall)
        wall = Wall(x= Scale.scale_x(500), y= Scale.scale_y(760), height= Scale.scale_y(500))
        self.walls.add(wall)
        
        platform_width = Scale.scale_x(100)
        x = Scale.scale_x(462)
        y = Scale.scale_y(280)
        platform = Platform(
            x=x,
            y=Display.HEIGHT - Physics.GROUND_HEIGHT - y,
            width=platform_width
        )
        self.platforms.add(platform)

        # wall three #
        wall = Wall(x = Scale.scale_x(750), y = Scale.scale_y(230), height= Scale.scale_y(200))
        self.walls.add(wall)
        wall = Wall(x = Scale.scale_x(750), y = Scale.scale_y(660), height= Scale.scale_y(500))
        self.walls.add(wall)
        
        platform_width = Scale.scale_x(100)
        x = Scale.scale_x(710)
        y = Scale.scale_y(380)
        platform = Platform(
            x=x,
            y=Display.HEIGHT - Physics.GROUND_HEIGHT - y,
            width=platform_width
        )
        self.platforms.add(platform)

        # wall four #
        wall = Wall(x = Scale.scale_x(950), y = Scale.scale_y(230), height= Scale.scale_y(200))
        self.walls.add(wall)
        wall = Wall(x = Scale.scale_x(950), y = Scale.scale_y(660), height= Scale.scale_y(500))
        self.walls.add(wall)
        
        platform_width = Scale.scale_x(100)
        x = Scale.scale_x(910)
        y = Scale.scale_y(380)
        platform = Platform(
            x=x,
            y=Display.HEIGHT - Physics.GROUND_HEIGHT - y,
            width=platform_width
        )
        self.platforms.add(platform)

        # wall five #
        
        # Top Wall #
        wall = Wall(x = Scale.scale_x(1150), y = Scale.scale_y(230), height= Scale.scale_y(440))
        self.walls.add(wall)
        # Bottom wall #
        wall = Wall(x = Scale.scale_x(1150), y= Scale.scale_y(860), height= Scale.scale_y(300))
        self.walls.add(wall)
        
        # Bottom Platform #
        platform_width = Scale.scale_x(100)
        x = Scale.scale_x(1110)
        y = Scale.scale_y(190)
        platform = Platform(
            x=x,
            y=Display.HEIGHT - Physics.GROUND_HEIGHT - y,
            width=platform_width
        )
        self.platforms.add(platform)

        # Top Platform #
        platform_width = Scale.scale_x(100)
        x = Scale.scale_x(1110)
        y = Scale.scale_y(360)
        platform = Platform(
            x=x,
            y=Display.HEIGHT - Physics.GROUND_HEIGHT - y,
            width=platform_width
        )
        self.platforms.add(platform)

        # Wall six #
        
        # Big Wall #
        wall = Wall(x = Scale.scale_x(1350), y = Scale.scale_y(330), height= Scale.scale_y(940))
        self.walls.add(wall)

        # Platforms #
        
        # Right Platform #
        platform_width = Scale.scale_x(100)
        x = Scale.scale_x(1310)
        y = Scale.scale_y(750)
        for i in range(3):
            platform = Platform(
                x = x,
                y = y,
                width = platform_width
            )
            self.platforms.add(platform)
            y -= Scale.scale_y(660) // 4

        # Left Platform #

        platform_width = Scale.scale_x(100)
        x = Scale.scale_x(1108)
        y = Scale.scale_y(500)
        for i in range(2):
            platform = Platform(
                x = x,
                y = y,
                width = platform_width
            )
            self.platforms.add(platform)
            y -= Scale.scale_y(660) // 4

        # Wall 7 #
        wall = Wall(x = Scale.scale_x(1500), y = Scale.scale_y(230), height= Scale.scale_y(940))
        self.walls.add(wall)

        # Red wall >:) #
        ground_spike = Spike(
            x=Scale.scale_x(1470),
            y=Scale.scale_y(220),
            width=Scale.scale_x(50),
            height=Scale.scale_y(20000)
        )
        self.spikes.add(ground_spike)

        # Ending :) #
        level_end = LevelEnd(
            x=Scale.scale_x(1400),
            y=Scale.scale_y(900),
            )
        self.level_ends.add(level_end)

