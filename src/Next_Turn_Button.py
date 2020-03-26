"""
Module Next_Turn_Button.py
============

This module contains class Info Button
"""

__version__ = '1.0'
__author__ = 'Edan Gurin'

'''
Kivy imports
'''

from kivy.core.audio import SoundLoader
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from src.constants import *

import os


class NextYear_Btn(ButtonBehavior, Image):
    """
    Class Method :
        Custom button for Game screen switch turns between user turn and AI
    """

    def __init__(self, **kwargs):
        """
        Function Method :
            initialize self and class param
            ===============================
        """
        super(NextYear_Btn, self).__init__(**kwargs)
        self.size_hint = (0.2, 0.1)  # size hint relative to window size
        self.border = (0, 0, 0, 0)  # border set to prevent incorrect rescalling
        self.pos = GetSystemMetrics(0) - GetSystemMetrics(0) / 4.5, 50  # position of the widget
        self.source = os.path.join('assets', 'images', '43_next_turn_u.png')  # source image for button

    def on_press(self):
        # on press event change source
        self.source = os.path.join('assets', 'images', '42_next_turn_d.png')

    def on_release(self):
        # on release event change image to og image
        self.source = os.path.join('assets', 'images', '43_next_turn_u.png')
        # if player score reached max score from all units - can switch to AI turn , else display error popup
        if self.parent.max_score == self.parent.score and self.parent.turn == self.parent.prev_turn:
            sound = SoundLoader.load('assets/audio/next_turn.mp3')
            sound.play()
            self.parent.update_year()
            self.parent.empire.update_diplomacy(self.parent.e1, self.parent.e2)
            self.parent.empire.update_treasury()
            self.parent.empire.update_manpower()
            self.parent.empire.update_stability()
            self.parent.update_labels(self.parent.empire)
            self.parent.empire1_play()
        else:
            sound = SoundLoader.load('assets/audio/button_click.mp3')
            sound.play()
            self.parent.UPDATESPopup('Need to Complete Tasks ')
