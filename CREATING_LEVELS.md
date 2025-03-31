# Level Creation Guide

## Table of Contents
1. [Game Objects](#game-objects)
2. [Creating a Level](#creating-a-level)
3. [Level One Example](#level-one-example)
4. [Best Practices](#best-practices)
5. [Version Control](#version-control)

## Game Objects

### Available Objects
1. **Platform**
   - Basic horizontal surface the player can stand on
   - Parameters: x, y, width
   ```python
   platform = Platform(x=100, y=200, width=300)
   ```

2. **Spike**
   - Object that kills the player
   - Parameters: x, y, width, height
   ```python
   spike = Spike(x=100, y=200, width=40, height=40)
   ```

3. **LevelEnd**
   - Object that completes the level when touched
   - Parameters: x, y
   ```python
   level_end = LevelEnd(x=100, y=200)
   ```

4. **Wall**
   - Similar to platforms, but vertical (you know what a fucking wall is)
   - Parameters: x, y, height
   ```python
   wall = Wall(x=100, y=200, height=300)
   ```

5. **Block**
    - Also similar to platform, but allows for a height arg as well as width
    - Parameters: x, y, width, height
    ```python
    block = block(x=100, y=200, height=300, width=300)

## Creating a Level

### Basic Structure
1. Create a new file in the `levels/` directory
2. Inherits from `BaseLevel`
3. Use the template below to implement `__init__` and `create_level`
4. Add level to `LEVELS` dictionary in `__init__.py`

```python
from .base_level import BaseLevel
from game_objects import Platform, Spike, LevelEnd

class LevelX(BaseLevel):
    def __init__(self):
        super().__init__()
        self.spawn_x = Scale.scale_x(200)  # Player spawn position
        self.spawn_y = Scale.scale_y(200)
        self.create_level()

    def create_level(self):
        # Add game objects here
        pass
```

`self.spawn_y` and `self.spawn_x` can be chnaged to suit your level

## Level One Example

### Code Breakdown
```python
def create_level(self):
    # Initialize platform dimensions
    platform_width = Scale.scale_x(300)
    x = Scale.scale_x(150)
    y = Scale.scale_y(200)

    # Create 4 platforms with increasing height
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
                width=Scale.scale_x(SpikeCfg.DEFAULT_WIDTH),
                height=Scale.scale_y(SpikeCfg.DEFAULT_HEIGHT)
            )
            self.spikes.add(spike)

        # Add level end on last platform
        if i == 3:
            level_end = LevelEnd(
                x=platform.rect.centerx - Images.level_end["WIDTH"] / 2,
                y=y - Images.level_end["HEIGHT"] / 2,
            )
            self.level_ends.add(level_end)

        # Increment position for next platform
        x += Scale.scale_x(450 + random.randint(0, 50))
        y += Scale.scale_y(50 + random.randint(0, 50))

    # Add ground spikes
    ground_spike = Spike(
        x=0,
        y=Display.HEIGHT - Physics.GROUND_HEIGHT - 1,
        width=Scale.scale_x(5000),
        height=Scale.scale_y(SpikeCfg.DEFAULT_HEIGHT)
    )
    self.spikes.add(ground_spike)
```

## Best Practices

1. **Scaling**
   - Use Scale.scale_x() and Scale.scale_y() for positioning on x and y coordinates respectively.
   - Also Use Scale.scale_x() and Scale.scale_y() for widths and heights respectively.
   - This ensures consistency across different screen resolutions

2. **Object Placement**
   - Keep platforms within reachable jumping distance (the level needs to be doable)
   - Maintain difficulty progression
   - Ensure level is completable

3. **Testing Checklist**
   - Player can reach all platforms
   - Level end is reachable
   - Spikes work correctly
   - No visual glitches
   - Consistent difficulty

## Version Control

### Branch Naming Convention
- Create a new branch for each level: `level-x` where x is the level number
- Example: `level-1`, `level-2`, etc.

### Development Flow
1. Create new level branch
```bash
git checkout -b level-x
```

2. Develop level
```bash
# Create level file
# Add to LEVELS dictionary
# Test thoroughly
```

3. Testing
- Complete playthrough testing
- Performance testing
- Edge case testing

4. Code Review
- Get review from team members
- Address feedback

5. Merge Process
```bash
git checkout dev
git pull origin dev
git merge level-x
git push origin dev
```

Always test the level thoroughly before merging to dev!
