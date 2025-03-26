import pygame
from pygame.constants import K_UP
from levels import Level
from player import Sprite
from config import Physics, Colours, Display, Player, AudioConfig
import time

# The entry point for the program

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.display.set_caption("white monster")
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(None, 74)
        self.current_level_number = 1
        self.current_level = Level(self.current_level_number)
        self.player = Sprite(
            self.current_level.platforms,
            self.current_level.spikes,
            self.current_level.level_ends
        )

    def switch_level(self):
        self.current_level_number += 1
        self.current_level = Level(self.current_level_number)
        self.player = Sprite(
            self.current_level.platforms,
            self.current_level.spikes,
            self.current_level.level_ends
        )

    def show_level_complete(self):
            self.screen.fill(Colours.BLACK)

            text = self.font.render(f"Level {self.current_level_number} Complete!", True, Colours.WHITE)
            text_rect = text.get_rect(center=(Display.WIDTH/2, Display.HEIGHT/2))

            self.screen.blit(text, text_rect)

            pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()

            # Update
            self.player.update()
            self.current_level.update()

            # Check if level is completed
            if self.player.check_level_end():
                time.sleep(0.3)
                self.player.audio.play_end_sound()
                self.show_level_complete()
                time.sleep(5)
                if self.current_level_number < 2: # Temporary, while we have two levels
                    self.switch_level()
                else:
                    self.running = False  # End game when all levels are complete
                continue

            # Draw
            self.screen.fill(Colours.BACKGROUND)
            self.current_level.draw(self.screen)
            self.screen.blit(self.player.image, self.player.rect)
            pygame.display.flip()

            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.move(-Player.NORMAL_SPEED)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.move(Player.NORMAL_SPEED)
        if keys[pygame.K_SPACE] or keys[K_UP]:
            self.player.jump()



if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
