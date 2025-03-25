import pygame
from pygame import mixer
import time
from config import HEIGHT, GROUND_HEIGHT, GRAVITY, JUMP_STRENGTH
from typing import Set

class Sprite(pygame.sprite.Sprite):
    def __init__(self, platforms_group, spikes_group, level_ends_group):
        super().__init__()
        self.image = pygame.image.load("./assets/img/sprite.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.start_x = 200
        self.start_y = HEIGHT - GROUND_HEIGHT - 200 - self.rect.height
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.vel_y = 0
        self.on_ground = False
        self.platforms = platforms_group
        self.spikes = spikes_group
        self.level_ends = level_ends_group
        self.reset()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def jump(self):
        if self.on_ground:
            self.play_jump_sound()

            self.vel_y -= JUMP_STRENGTH
            self.on_ground = False

    def check_platform_collisions(self):
        for platform in self.platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0 and self.rect.bottom - self.vel_y <= platform.rect.top + 10:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                    break
                elif self.vel_y < 0 and self.rect.top < platform.rect.bottom:
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0
                elif self.rect.right > platform.rect.left and self.rect.left < platform.rect.right:
                    if self.rect.centerx < platform.rect.centerx:
                        self.rect.right = platform.rect.left
                    else:
                        self.rect.left = platform.rect.right
        else:
            self.on_ground = False

    def update(self):
        level_end = 0
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y
        self.check_platform_collisions()
        if self.check_spike_collision():
            self.play_death_sound()
            time.sleep(0.3)
            self.reset()

        if self.check_level_end() and level_end < 1:
            level_end +=1
            self.play_end_sound()
            time.sleep(5)
            self.reset

        if self.rect.y >= HEIGHT - GROUND_HEIGHT - self.rect.height:
            self.rect.y = HEIGHT - GROUND_HEIGHT - self.rect.height
            self.vel_y = 0
            self.on_ground = True

    def check_spike_collision(self):
        for spike in self.spikes:
            if self.rect.colliderect(spike.rect):
                return True
        return False

    def check_level_end(self):
        for end in self.level_ends:
            if self.rect.colliderect(end.rect):
                return True
        return False


    def reset(self):
        self.rect.x = 200
        self.rect.y = HEIGHT - GROUND_HEIGHT - 200 - self.rect.height
        self.vel_y = 0

    def play_death_sound(self):
        mixer.init()
        mixer.music.load("assets/audio/death.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()

    def play_jump_sound(self):
        mixer.init()
        mixer.music.load("assets/audio/jump.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()

    def play_end_sound(self):
        mixer.init()
        mixer.music.load("assets/audio/end.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
