from pathlib import Path
from pygame import mixer
from config import VOLUME

class Audio():
    def __init__(self):
        self.death_sound = Path( Path.cwd() / "assets" / "audio" / "death.mp3")
        self.jump_sound = Path( Path.cwd() / "assets" / "audio" / "jump.mp3")
        self.end_sound = Path( Path.cwd() / "assets" / "audio" / "end3.mp3")

    def play_death_sound(self):
        mixer.init()
        mixer.music.load(self.death_sound)
        mixer.music.set_volume(VOLUME)
        mixer.music.play()

    def play_jump_sound(self):
        mixer.init()
        mixer.music.load(self.jump_sound)
        mixer.music.set_volume(VOLUME)
        mixer.music.play()

    def play_end_sound(self):
        mixer.init()
        mixer.music.load(self.end_sound)
        mixer.music.set_volume(VOLUME)
        mixer.music.play()
