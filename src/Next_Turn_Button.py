from kivy.core.audio import SoundLoader
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from src.constants import *
import os

class NextYear_Btn(ButtonBehavior, Image):

    def __init__(self, **kwargs):
        super(NextYear_Btn, self).__init__(**kwargs)
        self.size_hint = (0.2, 0.1)
        self.border = (0, 0, 0, 0)
        self.pos = GetSystemMetrics(0) - GetSystemMetrics(0) / 4.5, 50
        self.source = os.path.join('assets', 'images', '43_next_turn_u.png')

    def on_press(self):
        self.source = os.path.join('assets', 'images', '42_next_turn_d.png')

    def on_release(self):
        self.source = os.path.join('assets', 'images', '43_next_turn_u.png')
        if self.parent.max_score == self.parent.score and self.parent.turn == self.parent.prev_turn:
            sound = SoundLoader.load('assets/audio/next_turn.mp3')
            sound.play()
            self.parent.update_year()
            self.parent.empire.update_treasury()
            self.parent.empire.update_manpower()
            self.parent.empire.update_stability()
            self.parent.update_labels(self.parent.empire)
            self.parent.empire1_play()
        else:
            sound = SoundLoader.load('assets/audio/button_click.mp3')
            sound.play()
            self.parent.UPDATESPopup('Need to Complete Tasks ')
