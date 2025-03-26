import pygame
from pygame.constants import K_UP
from levels import Level
from player import Sprite
from config import BACKGROUND_COLOR, WIDTH, HEIGHT, NORMAL_SPEED, SPRINT_SPEED

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("white monster")
        self.clock = pygame.time.Clock()
        self.running = True

        self.current_level = Level(1)
        self.player = Sprite(
            self.current_level.platforms,
            self.current_level.spikes,
            self.current_level.level_ends
        )

    def run(self):
        while self.running:
            self.handle_events()

            # Update
            self.player.update()
            self.current_level.update()

            # Draw
            self.screen.fill(BACKGROUND_COLOR)
            self.current_level.draw(self.screen)
            self.screen.blit(self.player.image, self.player.rect)
            pygame.display.flip()

            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(-NORMAL_SPEED)
        if keys[pygame.K_RIGHT]:
            self.player.move(NORMAL_SPEED)
        if keys[pygame.K_SPACE] or keys[K_UP]:
            self.player.jump()
if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
