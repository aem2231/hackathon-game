from .base_level import BaseLevel
from game_objects import Platform, Spike, LevelEnd, Wall
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
        end_x = Scale.scale_x(1300)
        end_y = Scale.scale_y(650)

        end_platform = Platform(
            x=end_x, 
            y=end_y,
            width=end_width
            )
        self.platforms.add(end_platform)

        level_end = LevelEnd(
            x=end_platform.rect.centerx,
            y=end_platform.rect.top - Scale.scale_y(100)
            )
        self.level_ends.add(level_end)

        
        # Creating the actual level stuff.
        
        # Difficult jump one
        wall_lower_one = Wall(
            x=Scale.scale_x(500), 
            y=Scale.scale_y(700), 
            height=Scale.scale_y(400)
            )
        self.walls.add(wall_lower_one)

        wall_upper_one = Wall(
            x=Scale.scale_x(500), 
            y=Scale.scale_y(5), 
            height=Scale.scale_y(640)
            )
        self.walls.add(wall_upper_one)
        
        # Platform beyond jump one
        landing_width = Scale.scale_x(50)
        landing_x = Scale.scale_x(580)
        landing_y = Scale.scale_y(750)

        landing_platform_one = Platform(
            x=landing_x, 
            y=landing_y,
            width=landing_width
            )
        self.platforms.add(landing_platform_one)

        # Difficult jump two
        wall_lower_two = Wall(
            x=Scale.scale_x(700), 
            y=Scale.scale_y(690), 
            height=Scale.scale_y(390)
            )
        self.walls.add(wall_lower_two)

        wall_upper_two = Wall(
            x=Scale.scale_x(700), 
            y=Scale.scale_y(0), 
            height=Scale.scale_y(615)
            )
        self.walls.add(wall_upper_two)

        # Spike on lower wall
        spike = Spike(
                x=Scale.scale_x(700),
                y=Scale.scale_y(685),
                width=Scale.scale_x(25),
                height=Scale.scale_y(5)
            )
        self.spikes.add(spike)
        
        # Platform beyond jump two
        landing_width = Scale.scale_x(50)
        landing_x = Scale.scale_x(780)
        landing_y = Scale.scale_y(720)

        landing_platform_two = Platform(
            x=landing_x, 
            y=landing_y,
            width=landing_width
            )
        self.platforms.add(landing_platform_two)

        # Pole to continue to end
        pole_platform = Wall(
            x=Scale.scale_x(1070), 
            y=Scale.scale_y(690), 
            height=Scale.scale_y(400)
            )
        self.walls.add(pole_platform)

        pole_landing_width = Scale.scale_x(25)
        pole_landing_x = Scale.scale_x(1070)
        pole_landing_y = Scale.scale_y(685)

        pole_landing_platform = Platform(
            x=pole_landing_x, 
            y=pole_landing_y,
            width=pole_landing_width
            )
        self.platforms.add(pole_landing_platform)