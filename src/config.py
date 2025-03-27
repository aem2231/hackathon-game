import pygame

pygame.init()

class Scale:
    @staticmethod
    def scale(n):
        return (n / Display.BASE_WIDTH) * Display.HEIGHT

class Display:
    WIDTH = pygame.display.Info().current_w
    HEIGHT = pygame.display.Info().current_h
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
    BASE_GRAVITY = 0.9
    BASE_JUMP_STRENGTH = 20
    BASE_GROUND_HEIGHT = 50

    # Scaled values
    GRAVITY = BASE_GRAVITY * Display.SCALE
    JUMP_STRENGTH = BASE_JUMP_STRENGTH * Display.SCALE
    GROUND_HEIGHT = BASE_GROUND_HEIGHT * Display.SCALE

class Player:
    # Base values
    BASE_NORMAL_SPEED = 5
    BASE_SPRINT_SPEED = 10
    BASE_WIDTH = 45
    BASE_HEIGHT = 70

    # Scaled values
    NORMAL_SPEED = BASE_NORMAL_SPEED * Display.SCALE
    SPRINT_SPEED = BASE_SPRINT_SPEED * Display.SCALE
    WIDTH = Scale.scale(BASE_WIDTH)
    HEIGHT = Scale.scale(BASE_HEIGHT)
    STARTING_LIVES = 3

class AudioConfig:
    VOLUME = 0.7

class SpikeCfg:
    DEFAULT_HEIGHT = 50
    DEFAULT_WIDTH = 50
