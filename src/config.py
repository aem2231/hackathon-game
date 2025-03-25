import pygame

pygame.init()

# consnants

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
SURFACE_COLOR = (167, 255, 100)
GROUND_HEIGHT = 50
GRAVITY = 0.8
JUMP_STRENGTH = 20
NORMAL_SPEED = 5
SPRINT_SPEED = 10

RED = (255, 0, 0)
GROUND_COLOR = (100, 100, 100)
PLATFORM_COLOR = (100, 100, 100)
