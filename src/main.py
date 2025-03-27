import pygame
from pygame.constants import K_UP
from levels import get_level
from player import Sprite
from config import Colours, Display, Player
import time
from pathlib import Path
import json
from audio import Audio

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.display.set_caption("White Monster")
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(None, 74)

        self.audio = Audio()

        self.save_dir = Path( Path.cwd() / "save")
        self.save_file = Path( self.save_dir / "save.json")

        self.game_save = self.load_save()
        self.current_level_number = self.game_save["LEVEL"]

        self.show_title_screen()

        if self.current_level_number == 1:
            self.show_tutorial()
        self.current_level = get_level(self.current_level_number)
        self.player = Sprite(
            self.current_level.platforms,
            self.current_level.spikes,
            self.current_level.level_ends
        )

    def load_save(self):
        data = {}

        if not self.save_dir.is_dir():
            self.save_dir.mkdir()

        if not self.save_file.exists():
            with open(self.save_file, "w") as save:
                data = {
                    "LEVEL": 1
                }

                json.dump(data, save, indent = 4)

            return data

        try:
            with open(self.save_file, "r") as save:
                data = json.load(save)

            return data
        except:
            data = {
                "LEVEL": 1
            }

            return data


    def save_game(self, level):
        data = {
            "LEVEL": level
        }
        with open(self.save_file, "w") as save:
            json.dump(data, save, indent = 4)

    def switch_level(self):
        """Tries to switch to the next level. Returns False if there are no more levels."""
        self.current_level_number += 1
        self.save_game(self.current_level_number)
        try:
            self.current_level = get_level(self.current_level_number)
            self.player = Sprite(
                self.current_level.platforms,
                self.current_level.spikes,
                self.current_level.level_ends
            )
            return True
        except ValueError:
            return False

    def show_title_screen(self):
        title = "White Monster"
        displayed = ""
        x = Display.WIDTH/2
        y = Display.HEIGHT/2

        for letter in title:
            displayed += letter
            self.audio.play_boom_sound()
            self.screen.fill(Colours.BLACK)
            text = self.font.render(displayed, True, Colours.WHITE)
            text_rect = text.get_rect(center=(x, y))
            self.screen.blit(text, text_rect)
            pygame.display.flip()
            time.sleep(0.2)
        time.sleep(0.6)

        self.screen.fill(Colours.BLACK)

        try:
            title_image_path = Path(Path.cwd() / "assets" / "img" / "title.png")
            title_image = pygame.image.load(title_image_path)
            image_rect = title_image.get_rect(center=(x, y+100))
            self.screen.blit(title_image, image_rect)
            self.audio.play_boom_sound()
            pygame.display.flip()
            time.sleep(2)
        except:
            pass

    def show_tutorial(self):
        self.screen.fill(Colours.BLACK)


        controls = [
            "Use arrow keys / wasd to move!",
            "Use shift to sprint!",
            "Use space / up arrow to jump!",
            "Use ctrl to crouch!"
        ]

        objectives = [
            "Don't touch red",
            "Collect white monsters!"
        ]

        start_screen = [controls, objectives]

        for messages in start_screen:
            spacing = Display.HEIGHT / (len(messages) + 1)
            for i, message in enumerate(messages):
                text = self.font.render(message, True, Colours.WHITE)
                text_rect = text.get_rect(center=(Display.WIDTH/2, spacing * (i + 1)))
                self.screen.blit(text, text_rect)

                pygame.display.flip()
                self.audio.play_boom_sound()
                time.sleep(2)
            self.screen.fill(Colours.BLACK)


    def show_level_complete(self):
        self.screen.fill(Colours.BLACK)
        text = self.font.render(f"Level {self.current_level_number} Complete!", True, Colours.WHITE)
        text_rect = text.get_rect(center=(Display.WIDTH/2, Display.HEIGHT/2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def show_game_complete(self):
        self.screen.fill(Colours.BLACK)
        text = self.font.render("Hell Yeah! Game Complete!", True, Colours.WHITE)
        text_rect = text.get_rect(center=(Display.WIDTH/2, Display.HEIGHT/2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()

            # Update
            self.player.update()
            self.current_level.update()

            # Check if the level is completed
            if self.player.check_level_end():
                time.sleep(0.3)
                self.player.audio.play_end_sound()
                self.show_level_complete()
                time.sleep(5)

                # switch to next level
                if not self.switch_level():
                    # if theres no more levels, show game complete
                    self.show_game_complete()
                    self.save_game(1)
                    time.sleep(3)
                    self.running = False
                continue

            # Draw objects
            self.screen.fill(Colours.BACKGROUND)
            self.current_level.draw(self.screen)
            self.screen.blit(self.player.image, self.player.rect)
            pygame.display.flip()

            self.clock.tick(Display.FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.move(-Player.NORMAL_SPEED)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.move(Player.NORMAL_SPEED)
        if keys[pygame.K_SPACE] or keys[K_UP]:
            self.player.jump()
        if keys[pygame.K_RCTRL] or keys[pygame.K_LCTRL]:
            self.player.crouch()
        else:
            self.player.uncrouch()

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
