from .base_level import BaseLevel
from game_objects import Ground, Platform, Spike, LevelEnd, Wall, Block
from config import Physics, Display, Scale, SpikeCfg, Images

class Level2(BaseLevel):
    def __init__(self):
        super().__init__()
        self.spawn_x = Scale.scale_x(40)
        self.spawn_y = Display.HEIGHT - Physics.GROUND_HEIGHT - Scale.scale_y(SpikeCfg.DEFAULT_HEIGHT) - (Physics.GROUND_HEIGHT)
        self.create_level()

    def create_level(self):
        ground_spike = Spike(
            x=0,
            y=Display.HEIGHT - Physics.GROUND_HEIGHT - 1,
            width=Scale.scale_x(5000),
            height=Scale.scale_y(SpikeCfg.DEFAULT_HEIGHT)
        )
        self.spikes.add(ground_spike)

        wall_left = Wall(
            x = Scale.scale_x(300),
            y = Display.HEIGHT - Physics.GROUND_HEIGHT - Scale.scale_y(800),
            height= Scale.scale_y(800)
        )
        self.walls.add(wall_left)

        x = Physics.GROUND_HEIGHT // 2
        y = int(round(Display.HEIGHT - Physics.GROUND_HEIGHT - (Physics.GROUND_HEIGHT // 2)))

        width = 50

        for i in range(4):
            platform = Platform(
                x = x,
                y = y,
                width = Scale.scale_x(width)
            )
            self.platforms.add(platform)

            y -= Scale.scale_y(800) // 4


        x = wall_left.rect.left - Scale.scale_x(width)
        y = int(round(Display.HEIGHT - Physics.GROUND_HEIGHT - (Physics.GROUND_HEIGHT // 2) -  ((Scale.scale_y(800) // 4) // 2)))

        for i in range(4):
            platform = Platform(
                x = x,
                y = y,
                width = Scale.scale_x(width)
            )
            self.platforms.add(platform)

            y -= Scale.scale_y(800) // 4

        width = 500
        platform = Platform(
            x = wall_left.rect.right,
            y = Display.HEIGHT - Physics.GROUND_HEIGHT - Scale.scale_y(800),
            width= Scale.scale_x(width)
        )
        self.platforms.add(platform)

        height = 50
        wall = Wall(
            x = platform.rect.right,
            y = platform.rect.top,
            height = Scale.scale_y(height)
        )
        self.walls.add(wall)

        height = 1000
        wall_right = Wall(
            x = platform.rect.right + Scale.scale_x(100),
            y = Physics.GROUND_HEIGHT // 2 - Scale.scale_y(60),
            height = Scale.scale_y(height)
        )
        self.walls.add(wall_right)

        plat_width = 100
        for i in range(3):
            width = 550
            x = wall_right.rect.left - Scale.scale_x(width)
            if i == 1:
                x=wall_left.rect.right
            platform = Platform(
                x = x,
                y = platform.rect.centery + Scale.scale_y(200),
                width = Scale.scale_x(width)
                )
            self.platforms.add(platform)

            width = 660

            x = platform.rect.left
            if i == 1:
                x = platform.rect.left

            spike = Spike(
                x=x,
                y=platform.rect.top - 10,
                width=Scale.scale_x(width),
                height=Scale.scale_y(10)
            )
            self.spikes.add(spike)

            x = spike.rect.left
            if i != 1:
                x = wall_right.rect.left - Scale.scale_x(plat_width)

            for j in range(3):
                platform = Platform(
                    x = x,
                    y = spike.rect.top - Scale.scale_y(10),
                    width = Scale.scale_x(plat_width)
                )
                self.platforms.add(platform)
                if i == 1:
                    x+=Scale.scale_x(200)
                else:
                    x-=Scale.scale_x(200)
            plat_width -= 15

        platform = Platform(
            x=wall_left.rect.left,
            y=Display.HEIGHT - Physics.GROUND_HEIGHT - (Physics.GROUND_HEIGHT // 2),
            width = Scale.scale_x(800)
        )
        self.platforms.add(platform)

        block = Block(
            x = platform.rect.right,
            y = Display.HEIGHT - Physics.GROUND_HEIGHT - Scale.scale_y(100),
            width = Scale.scale_x(200),
            height = Scale.scale_y(100)
        )
        self.blocks.add(block)

        block = Block(
            x = block.rect.right + Scale.scale_x(200),
            y = Display.HEIGHT - Physics.GROUND_HEIGHT - Scale.scale_y(100),
            width = Scale.scale_x(200),
            height = Scale.scale_y(100)
        )
        self.blocks.add(block)

        platform = Platform(
            x =  Display.WIDTH - Scale.scale(100) - Physics.GROUND_HEIGHT // 2,
            y = Display.HEIGHT - Physics.GROUND_HEIGHT - Scale.scale_y(200),
            width = Scale.scale_x(100)
        )
        self.platforms.add(platform)

        level_end = LevelEnd(
            x = Display.WIDTH - Scale.scale_x(50) - Physics.GROUND_HEIGHT // 2,
            y = platform.rect.top - Scale.scale_y(100)
        )
        self.level_ends.add(level_end)
