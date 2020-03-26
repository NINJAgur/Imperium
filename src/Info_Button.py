"""
Module Info_Button.py
============

This module contains class Info Button
"""

__version__ = '1.0'
__author__ = 'Edan Gurin'

import os

'''
Kivy imports
'''

from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView


class Info_Button(Button):
    """
    Class Method :
        Custom button for Game screen mini - tutorial
    """
    def __init__(self, parent_widget, **kwargs):
        """
        Function Method :
            initialize self and class param
            ===============================

        :param parent_widget - original parent of the class - MainGame Screen
        """
        super(Info_Button, self).__init__(**kwargs)
        # scrollview widget to house layout with descriptions
        self.scrlv_info = ScrollView(size_hint=(0.5, 0.5), pos=(parent_widget.width / 3, parent_widget.height / 3))
        # original parent of the class - MainGame Screen
        self.parent_widget = parent_widget
        # border set to prevent incorrect rescalling
        self.border = (0, 0, 0, 0)
        # layout with GridLayout type to house Image descriptions with infinite height to accommodate scrlv
        self.layout = GridLayout(cols=1, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))

    def on_press(self):
        # sound play on button press event
        sound = SoundLoader.load('assets/audio/scrollview_click.mp3')
        sound.play()

    def on_release(self):
        # on button release event
        # adding city explanation images for Scrollview if no children exist for layout (user request to open sub- screen)
        if self.layout.children == []:
            self.scrlv_info.clear_widgets()

            self.layout.add_widget(Button(size_hint_y=None, height=500,
                                          background_normal=os.path.join('assets', 'images', '62_explanation1.png')))
            self.layout.add_widget(Button(size_hint_y=None, height=500,
                                          background_normal=os.path.join('assets', 'images', '63_explanation2.png')))
            self.layout.add_widget(Button(size_hint_y=None, height=500,
                                          background_normal=os.path.join('assets', 'images', '64_explanation3.png')))
            self.layout.add_widget(Button(size_hint_y=None, height=800,
                                          background_normal=os.path.join('assets', 'images', '65_explanation4.png')))
            self.layout.add_widget(Button(size_hint_y=None, height=600,
                                          background_normal=os.path.join('assets', 'images', '66_explanation5.png')))
            self.layout.add_widget(Button(size_hint_y=None, height=800,
                                          background_normal=os.path.join('assets', 'images', '67_explanation6.png')))
            self.layout.add_widget(Button(size_hint_y=None, height=500,
                                          background_normal=os.path.join('assets', 'images', '68_explanation7.png')))
            self.layout.add_widget(Button(size_hint_y=None, height=500,
                                          background_normal=os.path.join('assets', 'images', '69_explanation8.png')))
            self.scrlv_info.add_widget(self.layout)
            self.parent_widget.add_widget(self.scrlv_info)

        # else remove them (user cancels sub screen)
        else:
            self.parent_widget.remove_widget(self.scrlv_info)
            self.layout.clear_widgets()

    # update scrollview vertical values
    def scroll_change(self, scrlv, instance, value):
        scrlv.scroll_y = value

