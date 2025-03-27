# Level Creation Guide

## Table of Contents
1. [Preface](#preface)
2. [Basic Structure](#basic-structure)
3. [Game Objects](#game-objects)
4. [Creating a New Level](#creating-a-new-level)
5. [Example Levels](#example-levels)

## Preface

This guide should teach you everything you need to know to create a level. You should also take some time to familiarise yourself with and understand the codebase as this will make creating levels much easier.

When creating a level, you should checkout into a new branch called `level-i`, where `i` is the number of the level you are making. Once you have tested your level, merge it into dev. Always pull the latest commit from dev before you merge your level.

## Basic Structure

Each level is created as a separate class in the `levels` folder. The basic structure includes:
- Inherits from `BaseLevel`
- Ground (automatically added)
- Platforms
- Spikes
- Level end point

### Level Template
```python
from .base_level import BaseLevel
from game_objects import Platform, Spike, LevelEnd
from config import Physics, Display, Scale, SpikeCfg

class LevelX(BaseLevel):
    def __init__(self):
        super().__init__()  # Automatically adds ground
        self.create_level()

    def create_level(self):
        # Your level design here
        pass
```

## Game Objects

### Platform
```python
platform = Platform(x, y, width)
self.platforms.add(platform)
```
- `x`: X position (use `Scale.scale()`)
- `y`: Usually `Display.HEIGHT - Physics.GROUND_HEIGHT - Scale.scale(height)`
- `width`: Platform width (use `Scale.scale()`)

### Spike
```python
spike = Spike(x, y, width, height)
self.spikes.add(spike)
```
- `x`: X position (use `Scale.scale()`)
- `y`: Y position (use `Scale.scale()`)
- `width`: Usually `SpikeCfg.DEFAULT_WIDTH`
- `height`: Usually `SpikeCfg.DEFAULT_HEIGHT`

### Level End
```python
level_end = LevelEnd(x, y)
self.level_ends.add(level_end)
```
- `x`: X position (use `Scale.scale()`)
- `y`: Y position (use `Scale.scale()`)

## Creating a New Level

1. Create a new file in the `levels` folder (e.g., `level_three.py`):
```python
from .base_level import BaseLevel
from game_objects import Platform, Spike, LevelEnd
from config import Physics, Display, Scale, SpikeCfg

class Level3(BaseLevel):
    def __init__(self):
        super().__init__()
        self.create_level()

    def create_level(self):
        # Your level design here
        pass
```

2. Register the level in `levels/__init__.py`:
```python
from .level_three import Level3

LEVELS = {
    1: Level1,
    2: Level2,
    3: Level3,
}
```

## Example Levels

### Example Level 1: Platform Jumping
```python
class Level1(BaseLevel):
    def __init__(self):
        super().__init__()
        self.create_level()

    def create_level(self):
        x = Scale.scale(150)
        y = Scale.scale(200)

        for i in range(4):
            # Create platforms with increasing height
            platform = Platform(
                x=x,
                y=Display.HEIGHT - Physics.GROUND_HEIGHT - y,
                width=Scale.scale(200)
            )
            self.platforms.add(platform)

            # Add spikes on middle platforms
            if i != 0 and i != 3:
                spike = Spike(
                    x=platform.rect.centerx - Scale.scale(15),
                    y=platform.rect.centery - Scale.scale(30),
                    width=SpikeCfg.DEFAULT_WIDTH,
                    height=SpikeCfg.DEFAULT_HEIGHT
                )
                self.spikes.add(spike)

            # Add level end on last platform
            if i == 3:
                level_end = LevelEnd(
                    x=x + Scale.scale(120),
                    y=Display.HEIGHT - Physics.GROUND_HEIGHT - y - Scale.scale(110)
                )
                self.level_ends.add(level_end)

            x += Scale.scale(800)
            y += Scale.scale(100)
```

### Example Level 2: Vertical Challenge
```python
class Level2(BaseLevel):
    def __init__(self):
        super().__init__()
        self.create_level()

    def create_level(self):
        # Initial climbing section
        x, y = Scale.scale(200), Scale.scale(200)

        # Vertical platforms
        for i in range(4):
            platform = Platform(
                x=x,
                y=Display.HEIGHT - Physics.GROUND_HEIGHT - y,
                width=Scale.scale(200)
            )
            self.platforms.add(platform)
            y += Scale.scale(300)

        # Final challenge platform
        final_platform = Platform(
            x=Scale.scale(800),
            y=Display.HEIGHT - Physics.GROUND_HEIGHT - y,
            width=Scale.scale(200)
        )
        self.platforms.add(final_platform)

        # Level end
        level_end = LevelEnd(
            x=final_platform.rect.x + Scale.scale(70),
            y=final_platform.rect.y - Scale.scale(100)
        )
        self.level_ends.add(level_end)
```

## Tips for Level Design
1. **Scaling**
   - Always use `Scale.scale()` for x-coordinates and distances
   - Calculate y positions relative to ground: `Display.HEIGHT - Physics.GROUND_HEIGHT - Scale.scale(height)`

2. **Platform Placement**
   - Start with a safe landing platform
   - Ensure jumps are possible with player physics
   - Create interesting patterns and challenges

3. **Hazards**
   - Place spikes strategically
   - Create challenging but fair obstacles
   - Test all jump sequences

4. **Level End**
   - Place on final platform
   - Make it clearly reachable
   - Test completion sequence

5. **Testing**
   - Verify all jumps are possible
   - Check collision detection
   - Ensure level can be completed
   - Test with different screen resolutions
