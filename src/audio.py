from pathlib import Path
from pygame import mixer
from config import AudioConfig

class Audio():
    def __init__(self):
        self.death_sound = Path( Path.cwd() / "assets" / "audio" / "death.mp3")
        self.jump_sound = Path( Path.cwd() / "assets" / "audio" / "jump.mp3")
        self.end_sound = Path( Path.cwd() / "assets" / "audio" / "end.mp3")
        self.boom_sound = Path( Path.cwd() / "assets" / "audio" / "boom.mp3")

    def play_death_sound(self):
        mixer.init()
        mixer.music.load(self.death_sound)
        mixer.music.set_volume(AudioConfig.VOLUME)
        mixer.music.play()

    def play_jump_sound(self):
        mixer.init()
        mixer.music.load(self.jump_sound)
        mixer.music.set_volume(AudioConfig.VOLUME)
        mixer.music.play()

    def play_end_sound(self):
        mixer.init()
        mixer.music.load(self.end_sound)
        mixer.music.set_volume(AudioConfig.VOLUME)
        mixer.music.play()

    def play_boom_sound(self):
       mixer.init()
       mixer.music.load(self.boom_sound)
       mixer.music.set_volume(AudioConfig.VOLUME)
       mixer.music.play()
