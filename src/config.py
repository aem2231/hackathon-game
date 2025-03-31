import pygame

pygame.init()

class Scale:
    @staticmethod
    def scale(n):
        """
        Scales a given value proportionally based on the base width and current display height.

        Args:
            n (int): The value to be scaled.

        Returns:
            float/int: The scaled value.
        """
        return (n / Display.BASE_WIDTH) * Display.HEIGHT

    @staticmethod
    def scale_x(n):
        """
        Scales a given value proportionally based on the base width and current display width.

        Args:
            n (int): The value to be scaled.

        Returns:
            float/int: The scaled value.
        """
        return (n / Display.BASE_WIDTH) * Display.WIDTH

    @staticmethod
    def scale_y(n):
        """
        Scales a given value proportionally based on the base height and current display height.

        Args:
            n (int): The value to be scaled.

        Returns:
            float/int: The scaled value.
        """
        return (n / Display.BASE_HEIGHT) * Display.HEIGHT

class Display:
    # Preset resolutions
    RESOLUTIONS = {
        # Standard 16:9
        "HD": (1280, 720),        # 720p
        "FHD": (1920, 1080),      # 1080p
        "QHD": (2560, 1440),      # 1440p
        "4K": (3840, 2160),       # 2160p
        "8K": (7680, 4320),       # 4320p

        # Ultrawide 21:9
        "UW-FHD": (2560, 1080),   # Ultrawide 1080p
        "UW-QHD": (3440, 1440),   # Ultrawide 1440p
        "UW-5K": (5120, 2160),    # Ultrawide 4K

        # Super Ultrawide 32:9
        "SUW-FHD": (3840, 1080),  # Super Ultrawide 1080p
        "SUW-QHD": (5120, 1440),  # Super Ultrawide 1440p

        # Common Laptop 16:10
        "WXGA": (1280, 800),      # Common laptop
        "WSXGA+": (1680, 1050),   # Common laptop
        "WUXGA": (1920, 1200),    # Common laptop
        "MacBook": (2560, 1600),  # MacBook Pro 13"

        # Square-ish 4:3
        "SVGA": (800, 600),       # Classic monitor
        "XGA": (1024, 768),       # Classic monitor
        "SXGA": (1280, 1024),     # Classic monitor

        # Tablet/iPad-like 3:2
        "Surface": (2736, 1824),  # Surface Pro
        "iPad": (2048, 1536),     # iPad

        # Phone-like formats
        "iPhone": (1170, 2532),   # iPhone 13 Pro
        "Android": (1440, 3040),  # Samsung S10

        # Smaller screens
        "Small": (300, 300),      # Unplayable (ish)
        "Minimum": (800, 600),    # Minimum playable

        # Other common
        "WXGA+": (1440, 900),     # Common laptop
        "WQHD+": (3440, 1600),    # Dell Ultrawide
        "5K": (5120, 2880),       # iMac 27"
        "6K": (6016, 3384)        # Pro Display XDR
    }

    # Set this to False for windowed mode
    FULLSCREEN = False

    # Default resolution (can be changed)
    CURRENT_RESOLUTION = "HD"
    # Get current resolution values
    WIDTH = RESOLUTIONS[CURRENT_RESOLUTION][0] if not FULLSCREEN else pygame.display.Info().current_w
    HEIGHT = RESOLUTIONS[CURRENT_RESOLUTION][1] if not FULLSCREEN else pygame.display.Info().current_h

    BASE_WIDTH = 1920
    BASE_HEIGHT = 1080
    SCALE__X = WIDTH / BASE_WIDTH
    SCALE__Y = HEIGHT / BASE_HEIGHT
    SCALE = min(SCALE__X, SCALE__Y)
    FPS = 60
    CAPTION = "White Monster"

class Colours:
    SURFACE = (167, 255, 100)
    RED = (255, 0, 0)
    BLUE = (166, 243, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BACKGROUND = (181, 181, 181)
    GROUND = (100, 100, 100)
    PLATFORM = (100, 100, 100)

class Physics:
    BASE_GRAVITY = 1
    BASE_JUMP_STRENGTH = 16
    BASE_GROUND_HEIGHT = 50

    # Scaled values
    GRAVITY = BASE_GRAVITY * Display.SCALE
    JUMP_STRENGTH = BASE_JUMP_STRENGTH * Display.SCALE
    GROUND_HEIGHT = BASE_GROUND_HEIGHT * Display.SCALE__Y

class Player:
    # Base values
    BASE_NORMAL_SPEED = 5
    BASE_SPRINT_SPEED = 10
    BASE_WIDTH = 30
    BASE_HEIGHT = 55

    # Scaled values
    NORMAL_SPEED = BASE_NORMAL_SPEED * Display.SCALE__X
    SPRINT_SPEED = BASE_SPRINT_SPEED * Display.SCALE__X
    WIDTH = Scale.scale_x(BASE_WIDTH)
    HEIGHT = Scale.scale_y(BASE_HEIGHT)
    STARTING_LIVES = 3

class AudioConfig:
    VOLUME = 0.7

class SpikeCfg:
    DEFAULT_HEIGHT = 40
    DEFAULT_WIDTH = 40

class Images:
    level_end = {
        "HEIGHT": 46,
        "WIDTH": 95
    }
