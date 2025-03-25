import pygame
import random
from player import Sprite
from game_objects import LevelEnd, Platform, Ground, Spike
from config import HEIGHT, WIDTH, GROUND_HEIGHT, SPRINT_SPEED, NORMAL_SPEED

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Side-Scrolling Platformer")

background = pygame.image.load("./assets/img/background.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

platforms = pygame.sprite.Group()
spikes = pygame.sprite.Group()
level_ends = pygame.sprite.Group()

ground = Ground(0, WIDTH * 2)
platforms.add(ground)

x = 200
y = 200

for i in range(4):
    platform = Platform(x, HEIGHT - GROUND_HEIGHT - y, 200)
    platforms.add(platform)

    if i == 3:
        level_end = LevelEnd(x+70, HEIGHT - GROUND_HEIGHT - y - 100)
        level_ends.add(level_end)

    x+=500 + random.randint(0, 100)
    y+=100 + random.randint(0, 100)

x=0
for i in range(100):
    spike = Spike(x, HEIGHT - GROUND_HEIGHT - 120)
    spikes.add(spike)
    x += (300 - random.randint(5,20))

playerCar = Sprite(platforms, spikes, level_ends)
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(playerCar)


running = True
clock = pygame.time.Clock()

while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                playerCar.jump()

    keys = pygame.key.get_pressed()
    speed = SPRINT_SPEED if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] else NORMAL_SPEED

    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(speed)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(speed)

    all_sprites_list.update()
    platforms.update()

    screen.blit(background, (0, 0))
    platforms.draw(screen)
    spikes.draw(screen)
    level_ends.draw(screen)
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
