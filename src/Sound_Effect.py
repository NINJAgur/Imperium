"""
Module Sound_Effect.py
============

This module function for click sound effect
"""

__version__ = '1.0'
__author__ = 'Edan Gurin'

'''
Kivy imports
'''

from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.togglebutton import ToggleButton


def play_sound(event) :
    """
    Function Method :
        initialize triggered on event (mainly press / release)
        ======================================================
    :param event: press event of some sort of button
    """
    sound = ObjectProperty(None, allownone=True) # ObjectProperty() - Property that represents a Python object.
    volume = NumericProperty(1.0)                # NumericProperty()- Property that represents integer value for sound
    if type(event) != ToggleButton : # if button clicked is not selection button for empire in selection screen
        sound = SoundLoader.load('assets/audio/button_click.mp3')
        sound.play()
    else :
        sound = SoundLoader.load('assets/audio/empire_select.mp3')
        sound.play()





