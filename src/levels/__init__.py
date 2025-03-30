from .level_one import Level1
from .level_two import Level2

LEVELS = {
    1: Level1,
    2: Level2
    # Add more levels here as needed
}

def get_level(level_number):
    """Factory function to create level instances"""
    level_class = LEVELS.get(level_number)
    if level_class is None:
        raise ValueError(f"Level {level_number} does not exist")
    return level_class()
