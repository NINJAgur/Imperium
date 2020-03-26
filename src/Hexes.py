"""
Module Hexes.py
====================================================================================

This module contains the classes that represents graphically the hexagonal tiles of the Board
"""

__version__ = '1.0'
__author__ = 'Edan Gurin'

'''
KIVY 1.11.0 IMPORTED PACKAGES
'''
from kivy.core.image import Image as CoreImage
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

import os
from src.constants import *


class HexTile(ButtonBehavior, Image):
    """
    Class Method :
        Mixin ButtonBehavior with Images kivy classes
        Hextile class represents terrain tiles only.
        Unchangeable sources for hex tiles.
    """

    def __init__(self, pos, loc, type, **kwargs):
        """
            Function Method :
            initialize self and class param
            ===============================
                :param pos: pos of class
                :param loc: tuple loc of the class
                :param type: string value defining the source for class
        """
        super(HexTile, self).__init__(**kwargs)
        self.size = GetSystemMetrics(0) / POS_Y, GetSystemMetrics(1) / POS_X  # the size of the hex: (width, height)
        self.pos = pos
        self.loc = loc
        self.type = type
        if self.type == "Grasslands":
            if self.loc[0] < 25:
                self.source = os.path.join('assets', 'images', '18_hex_green.png')
            else :
                self.source = os.path.join('assets', 'images', '18_hex_green_alt.png')
        if self.type == "Desert":
            self.source = os.path.join('assets', 'images', '19_hex_yellow.png')

        if self.type == "Sea":
            self.source = os.path.join('assets', 'images', '20_hex_blue.png')

        if self.type == "Mountains":
            self.source = os.path.join('assets', 'images', '38_hex_brown.png')

        if self.type == "City":
            self.source = os.path.join('assets', 'images', '39_hex_grey.png')

        if self.type == "pass":
            self.source = os.path.join('assets', 'images', '61_water_pass.png')


'''------------------------------------------------------------------------------------------------------------------'''


class Empire_HexTile(ButtonBehavior, Image):
    """
    Class Method :
        Mixin ButtonBehavior with Images kivy classes This class is built in on top HexTile for source
        changes and can contain empire specific tiles beside regular tiles.
    """
    def __init__(self, pos, loc, type, **kwargs):
        """
        Function Method :
        initialize self and class param
        ===============================
            :param pos: pos of class
            :param loc: tuple loc of the class
            :param type: string value defining the source for class
        """
        super(Empire_HexTile, self).__init__(**kwargs)
        self.size = GetSystemMetrics(0) / POS_Y, GetSystemMetrics(1) / POS_X  # the size of the hex: (width, height)
        self.pos = pos
        self.loc = loc
        self.occupied = False
        # LOC IS INVERTED NOW HEIGHT, WIDTH
        self.background = CoreImage(os.path.join('assets', 'images', 'finalmap.png'))
        self.type = type
        if self.type == "Roman":
            self.source = os.path.join('assets', 'images', '35_rome_hex.png')
        elif self.type == "Carthaginian":
            self.source = os.path.join('assets', 'images', '36_carthage_hex.png')
        elif self.type == "Egyptian":
            self.source = os.path.join('assets', 'images', '37_egypt_hex.png')
        elif self.type == "Grasslands":
            if self.loc[0] < 25:
                self.source = os.path.join('assets', 'images', '18_hex_green.png')
            else:
                self.source = os.path.join('assets', 'images', '18_hex_green_alt.png')
        elif self.type == "Desert":
            self.source = os.path.join('assets', 'images', '19_hex_yellow.png')
        elif self.type == "Sea":
            self.source = os.path.join('assets', 'images', '20_hex_blue.png')
        elif self.type == "Mountains":
            self.source = os.path.join('assets', 'images', '38_hex_brown.png')
        elif self.type == "City":
            self.source = os.path.join('assets', 'images', '39_hex_grey.png')
        elif self.type == "white":
            self.source = os.path.join('assets', 'images', '60_hex_white.png')
        elif self.type == "pass":
            self.source = os.path.join('assets', 'images', '61_water_pass.png')


'''------------------------------------------------------------------------------------------------------------------'''
