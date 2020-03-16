import os

from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.button import Button


class MenuAudioButton(Button):
    sound = ObjectProperty(None, allownone=True)
    volume = NumericProperty(1.0)
    sound = SoundLoader.load(os.path.join('assets', 'audio', 'menu_music.mp3'))

    def on_release(self):
        if self.sound is None or self.sound.status == 'stop':
            self.sound = SoundLoader.load(os.path.join('assets', 'audio', 'menu_music.mp3'))
            self.sound.play()
            self.sound.volume = self.volume
        else:
            self.sound.stop()
