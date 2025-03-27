import pygame
import time
from config import Physics, Colours, Display, Player
from audio import Audio

class Sprite(pygame.sprite.Sprite):
    def __init__(self, platforms_group, spikes_group, level_ends_group):
        super().__init__()
        self.original_height = Player.HEIGHT
        self.is_crouching = False
        self.image = pygame.Surface((int(Player.WIDTH), int(Player.HEIGHT)))
        self.image.fill(Colours.BLUE)
        self.rect = self.image.get_rect()
        self.start_x = 200
        self.start_y = Display.HEIGHT - Physics.GROUND_HEIGHT - 200 - self.rect.height
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.vel_y = 0
        self.on_ground = False
        self.platforms = platforms_group
        self.spikes = spikes_group
        self.level_ends = level_ends_group
        self.reset()
        self.audio = Audio()

    def move(self, pixels):
        if pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT]:
            self.rect.x += pixels * (Player.SPRINT_SPEED / Player.NORMAL_SPEED)
        else:
            self.rect.x += pixels

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def jump(self):
        if self.on_ground:
            self.audio.play_jump_sound()

            self.vel_y -= Physics.JUMP_STRENGTH
            self.on_ground = False

    def crouch(self):
        if not self.is_crouching:
            bottom = self.rect.bottom
            left = self.rect.left
            new_height = round(self.original_height / 1.5, 1)

            self.image = pygame.Surface((int(Player.WIDTH), int(new_height)))
            self.image.fill(Colours.BLUE)

            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
            self.rect.left = left
            self.is_crouching = True

    def uncrouch(self):
        if self.is_crouching:
            bottom = self.rect.bottom
            left = self.rect.left

            self.image = pygame.Surface((int(Player.WIDTH), int(self.original_height)))
            self.image.fill(Colours.BLUE)

            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
            self.rect.left = left
            self.is_crouching = False

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
        self.vel_y += Physics.GRAVITY
        self.rect.y += self.vel_y
        self.check_platform_collisions()
        if self.check_spike_collision():
            self.audio.play_death_sound()
            time.sleep(0.3)
            self.reset()

        if self.rect.y >= Display.HEIGHT - Physics.GROUND_HEIGHT - self.rect.height:
            self.rect.y = Display.HEIGHT - Physics.GROUND_HEIGHT - self.rect.height
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
        self.rect.y = Display.HEIGHT - Physics.GROUND_HEIGHT - 200 - self.rect.height
        self.vel_y = 0
