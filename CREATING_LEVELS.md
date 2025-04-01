# Level Creation Guide

## Table of Contents
1. [Quick Start](#quick-start)
2. [Core Concepts](#core-concepts)
   - [Coordinate System](#1-coordinate-system)
   - [Game Objects](#2-game-objects)
   - [Important Measurements](#3-important-measurements)
3. [Best Practices](#best-practices)
   - [Level Structure](#1-level-structure)
   - [Helper Methods](#2-helper-methods)
   - [Level Difficulty Guidelines](#3-level-difficulty-guidelines)
   - [Common Patterns](#4-common-patterns)
4. [Game Objects Reference](#game-objects-reference)
   - [Base Objects](#1-base-objects)
   - [BaseLevel Class](#2-baselevel-class)
   - [Scaling System](#3-scaling-system)
   - [Level Example](#4-level-example)
   - [Common Level Patterns](#5-common-level-patterns)
5. [Testing & Debugging](#testing--debugging)
   - [Playtest Checklist](#1-playtest-checklist)
   - [Common Issues](#2-common-issues)
   - [Debug Tips](#3-debug-tips)
6. [Version Control](#version-control)

## Game Objects Reference

### 1. Base Objects
#### Ground
- Creates a horizontal surface at the bottom of the screen
- Usage:
```python
ground = Ground(x=0, width=Display.WIDTH)
self.platforms.add(ground)
```

#### Platform
- Horizontal surfaces players can stand on
- Usage:
```python
platform = Platform(
    x=Scale.scale_x(100),    # X position
    y=Scale.scale_y(500),    # Y position
    width=Scale.scale_x(300) # Width of platform
)
self.platforms.add(platform)
```

#### Wall
- Vertical barriers
- Usage:
```python
wall = Wall(
    x=Scale.scale_x(500),     # X position
    y=Scale.scale_y(200),     # Y position
    height=Scale.scale_y(400) # Height of wall
)
self.walls.add(wall)
```

#### Spike
- Hazards that reset the player on contact
- Usage:
```python
spike = Spike(
    x=Scale.scale_x(300),         # X position
    y=Scale.scale_y(700),         # Y position
    width=Scale.scale_x(40),      # Width of spike
    height=Scale.scale_y(40)      # Height of spike
)
self.spikes.add(spike)
```

#### LevelEnd
- Goal object that completes the level when touched
- Usage:
```python
level_end = LevelEnd(
    x=Scale.scale_x(1800),  # X position
    y=Scale.scale_y(500)    # Y position
)
self.level_ends.add(level_end)
```

#### Block
- Solid rectangular obstacles
- Usage:
```python
block = Block(
    x=Scale.scale_x(600),      # X position
    y=Scale.scale_y(300),      # Y position
    width=Scale.scale_x(100),  # Width of block
    height=Scale.scale_y(100)  # Height of block
)
self.blocks.add(block)
```

### 2. BaseLevel Class
The BaseLevel class provides the foundation for all levels:

```python
class BaseLevel:
    def __init__(self):
        # Sprite Groups for different game objects
        self.platforms = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.level_ends = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()

        # Creates world boundaries
        boundaries = WorldBoundaries()
        self.walls.add(boundaries.left_wall)
        self.walls.add(boundaries.right_wall)

        # Creates ground
        ground = Ground(0, Display.WIDTH * 2)
        self.platforms.add(ground)
```

### 3. Scaling System
The game uses a scaling system to maintain consistent proportions across different screen sizes:

```python
# Example of scaling usage
Scale.scale_x(100)   # Scales horizontally based on screen width
Scale.scale_y(100)   # Scales vertically based on screen height
Scale.scale(100)     # Scales uniformly (uses minimum of x/y scale) (avoid using this)
```

### 4. Level Example
Here's a simple level example with common patterns:

```python
class ExampleLevel(BaseLevel):
    def __init__(self):
        super().__init__()
        self.spawn_x = Scale.scale_x(100)  # Player spawn X
        self.spawn_y = Scale.scale_y(500)  # Player spawn Y
        self.create_level()

    def create_level(self):
        # Create starting platform
        start_platform = Platform(
            x=Scale.scale_x(50),
            y=Scale.scale_y(600),
            width=Scale.scale_x(200)
        )
        self.platforms.add(start_platform)

        # Create hazard
        spike = Spike(
            x=Scale.scale_x(300),
            y=Scale.scale_y(750),
            width=Scale.scale_x(100),
            height=Scale.scale_y(40)
        )
        self.spikes.add(spike)

        # Create goal platform and end point
        end_platform = Platform(
            x=Scale.scale_x(500),
            y=Scale.scale_y(400),
            width=Scale.scale_x(150)
        )
        self.platforms.add(end_platform)

        level_end = LevelEnd(
            x=end_platform.rect.centerx,
            y=end_platform.rect.top - Scale.scale_y(100)
        )
        self.level_ends.add(level_end)
```

### 5. Common Level Patterns

#### Platform Sequence
```python
# Creating a sequence of ascending platforms
x = Scale.scale_x(100)
y = Scale.scale_y(700)
for i in range(5):
    platform = Platform(
        x=x,
        y=y,
        width=Scale.scale_x(100)
    )
    self.platforms.add(platform)
    x += Scale.scale_x(200)
    y -= Scale.scale_y(100)
```

#### Hazard Zone
```python
# Creating a hazardous area
ground_spike = Spike(
    x=0,
    y=Display.HEIGHT - Physics.GROUND_HEIGHT - 1,
    width=Scale.scale_x(5000),
    height=Scale.scale_y(40)
)
self.spikes.add(ground_spike)
```

#### Vertical Challenge
```python
# Creating a vertical climbing section
wall_left = Wall(
    x=Scale.scale_x(300),
    y=Scale.scale_y(200),
    height=Scale.scale_y(400)
)
self.walls.add(wall_left)

wall_right = Wall(
    x=Scale.scale_x(500),
    y=Scale.scale_y(200),
    height=Scale.scale_y(400)
)
self.walls.add(wall_right)
```

## Version Control

### 1. Branch Management
```bash
# Create new level branch
git checkout -b level-5

# Update from development
git checkout dev
git pull origin dev
git checkout level/level-5
git merge level-5
```

### 2. Naming Conventions
```
Branches:
- level/level-{number}         # New level
- level/modify-{number}        # Level modifications
- level/bugfix-{number}        # Level-specific fixes
```

### 3. Development Workflow
1. **Branch Creation**
   ```bash
   git checkout -b level-5
   ```

2. **Initial Setup**
   ```python
   # levels/__init__.py
   from .level_five import Level5

   LEVELS = {
       # ... existing levels ...
       5: Level5,
   }
   ```

3. **Development Cycle**
   ```bash
   # Make changes
   git add .
   git commit -m "(level-5): Add initial platform layout"

   # Regular testing
   git push origin level/level-5
   ```

4. **Code Review Process**
   - Ask others for feedback
   - Address review comments

### 4. Asset Management
```
levels/
├── __init__.py
├── base_level.py
├── level_1.py
├── level_2.py
└── assets/
    ├── img
    ├── audio
```

### 5. Review Checklist
- [ ] Code follows style guide
- [ ] Level difficulty fits progression
- [ ] Documentation updated if needed
- [ ] Playtest feedback addressed

### 6. Hotfix Process
```bash
# For critical level bugs
git checkout -b level/hotfix-5
# Make fixes
git commit -m "fix(level-5): Fix impossible jump sequence"
git push origin level/hotfix-5
