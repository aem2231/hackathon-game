import pygame

pygame.init()

class Display:
    WIDTH = pygame.display.Info().current_w
    HEIGHT = pygame.display.Info().current_h
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
    GRAVITY = 0.8
    JUMP_STRENGTH = 20
    GROUND_HEIGHT = 50

class Player:
    NORMAL_SPEED = 5
    SPRINT_SPEED = 10
    WIDTH = 45
    HEIGHT = 70
    STARTING_LIVES = 3

class AudioConfig:
    VOLUME = 0.7
