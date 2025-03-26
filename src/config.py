import pygame

pygame.init()

class Display:
    WIDTH = pygame.display.Info().current_w
    HEIGHT = pygame.display.Info().current_h
    BASE_WIDTH = 2560
    BASE_HEIGHT = 1600
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
    BASE_GRAVITY = 0.8
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
    WIDTH = BASE_WIDTH * Display.SCALE
    HEIGHT = BASE_HEIGHT * Display.SCALE
    STARTING_LIVES = 3

class AudioConfig:
    VOLUME = 0.7
