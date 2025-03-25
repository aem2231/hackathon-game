import pygame
from player import Sprite
from game_objects import Platform, Ground
from config import HEIGHT, WIDTH, GROUND_HEIGHT, SPRINT_SPEED, NORMAL_SPEED

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Side-Scrolling Platformer")

background = pygame.image.load("./assets/background.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

platforms = pygame.sprite.Group()

ground = Ground(0, WIDTH * 2)
platforms.add(ground)

platform = Platform(300, HEIGHT - GROUND_HEIGHT - 200, 200)
platforms.add(platform)

platform = Platform(800, HEIGHT - GROUND_HEIGHT - 300, 200)
platforms.add(platform)


playerCar = Sprite(platforms)
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
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
