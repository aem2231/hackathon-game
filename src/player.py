import pygame
from config import WIDTH, HEIGHT, GROUND_HEIGHT, GRAVITY, JUMP_STRENGTH

class Sprite(pygame.sprite.Sprite):
    def __init__(self, platforms_group, spikes_group):
        super().__init__()
        self.image = pygame.image.load("./assets/sprite.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 4
        self.rect.y = HEIGHT - GROUND_HEIGHT - self.rect.height
        self.vel_y = 0
        self.on_ground = False
        self.platforms = platforms_group
        self.spikes = spikes_group

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def jump(self):
        if self.on_ground:
            self.vel_y -= JUMP_STRENGTH
            self.on_ground = False

    def check_platform_collisions(self):
        for platform in self.platforms:
            if self.rect.colliderect(platform.rect) and self.vel_y > 0:
                self.rect.bottom = platform.rect.top
                self.vel_y = 0
                self.on_ground = True
                break
        else:
            self.on_ground = False

    def update(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y
        self.check_platform_collisions()
        if self.check_spike_collision:
            self.kill()
            self.rect.y = 100
        if self.rect.y >= HEIGHT - GROUND_HEIGHT - self.rect.height:
            self.rect.y = HEIGHT - GROUND_HEIGHT - self.rect.height
            self.vel_y = 0
            self.on_ground = True

    def check_spike_collision(self):
        for spike in self.spikes:
            return self.rect.colliderect(spike.rect)
