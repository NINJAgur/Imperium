"""
Module Audio_Button.py
============

This module contains class MenuAudioButton
"""

__version__ = '1.0'
__author__ = 'Edan Gurin'

import os
'''
Kivy imports
'''
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty
from kivy.uix.button import Button


class MenuAudioButton(Button):
    """
    Class Method :
        Custom button for menu sound playback
    """
    volume = NumericProperty(1.0) # Property that represents a numeric value of volume
    sound = SoundLoader.load(os.path.join('assets', 'audio', 'menu_music.mp3')) # kivy.core.audio.audio_gstplayer. SoundGstplayer object with loaded mp3 file

    def on_release(self):
        """
        Trigger when button class is pressed - on release music is released or stops
        if currently there is no sound or it is stopped :
            play sound
        else
            stop sound
        """
        if self.sound is None or self.sound.status == 'stop':
            self.sound = SoundLoader.load(os.path.join('assets', 'audio', 'menu_music.mp3'))
            self.sound.play()
            self.sound.volume = self.volume
        else:
            self.sound.stop()
