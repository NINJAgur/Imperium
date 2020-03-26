"""
Module Units.py
============

This module contains classes of units - Empire_Unit, Empire_Warship and Empire_Worker
"""

__version__ = '1.0'
__author__ = 'Edan Gurin'

'''
Kivy imports
'''
from kivy.uix.behaviors import ToggleButtonBehavior

'''
src imports
'''
from src.Hexes import *


class Empire_Warship(ToggleButtonBehavior, Image):
    """
    Class Method :
        Mixin ToggleButtonBehavior with Images kivy classes
        The Toggle Button widget acts like a checkbox. When you touch or click it, the state toggles between ‘normal’
        and ‘down’ (as opposed to a Button that is only ‘down’ as long as it is pressed).
        The Empire warship is the naval unit for each empire with the shore unit deployment ability.
    """
    def __init__(self, pos, loc, name, **kwargs):
        """
        Function Method :
            initialize self and class param
            ===============================
            :param pos: pos of the class
            :param loc: tuple loc of the class
            :param name: name of parent empire
        """
        super(Empire_Warship, self).__init__(**kwargs)
        self.pos = pos  # pos in the canvas
        self.size = (GetSystemMetrics(0) / POS_Y / 1.3, GetSystemMetrics(1) / POS_X / 1.3)  # size in the canvas
        self.loc = loc  # tuple location on board
        self.name = name  # empire name
        self.score = 0  # score - each unit has personal score value (max 3) which allows it to do certain actions
        self.power = 0  # manpower value - defines unit's strength on the battlfield
        self.pressed = False  # boolean value to check unit is currently pressed
        self.arr = []  # list to contain white hexes for movement
        self.class_name = 'S' # first letter of class name (for id)
        # configuration for source based on empire
        if name == "Rome":
            self.source = os.path.join('assets', 'images', '44_rome_ship.png')
        elif name == "Carthage":
            self.source = os.path.join('assets', 'images', '45_carthage_ship.png')
        else:
            self.source = os.path.join('assets', 'images', '46_egypt_ship.png')

    def on_state(self, widget, value):
        """
        Triggers on pressing of the Unit
        :param widget: self
        :param value: current state of the Toggle Button
        """
        if value == 'normal':
            # reset opacity
            self.opacity = 1
            # remove all white hexes from board
            self.remove_tiles()

        elif value == 'down':
            # if left clicked on unit
            if self.parent.touch.button == 'left':
                #set new opacity
                self.opacity = 0.5
                # create hexes around the unit where it can go - check their validity with valid()
                if self.loc[1] % 2 == 0:
                    for i in range(self.loc[0], self.loc[0] + 2):
                        for j in range(self.loc[1] - 1, self.loc[1] + 2):
                            if j % 2 == 0:
                                pos = (j * 45, 26 + 50 / 2 + i * 50)
                            else:
                                pos = (j * 45, 26 + i * 50)

                            if (self.loc[0] != i or self.loc[1] != j) and self.valid(self, i, j):
                                hex = Empire_HexTile(pos, (i, j), "white")
                                self.arr.append(hex)
                                self.parent.add_widget(hex)

                    if self.valid(self, self.loc[0] - 1, self.loc[1]):
                        hex = Empire_HexTile((self.loc[1] * 45, 26 + 50 / 2 + (self.loc[0] - 1) * 50),
                                             (self.loc[0] - 1, self.loc[1]), "white")
                        self.arr.append(hex)
                        self.parent.add_widget(hex)

                else:
                    for i in range(self.loc[0] - 1, self.loc[0] + 1):
                        for j in range(self.loc[1] - 1, self.loc[1] + 2):
                            if j % 2 == 0:
                                pos = (j * 45, 26 + 50 / 2 + i * 50)
                            else:
                                pos = (j * 45, 26 + i * 50)

                            if (self.loc[0] != i or self.loc[1] != j) and self.valid(self, i, j) == True:
                                hex = Empire_HexTile(pos, (i, j), "white")
                                self.arr.append(hex)
                                self.parent.add_widget(hex)

                    if self.valid(self, self.loc[0] + 1, self.loc[1]):
                        hex = Empire_HexTile((self.loc[1] * 45, 26 + (self.loc[0] + 1) * 50),
                                             (self.loc[0] - 1, self.loc[1]), "white")
                        self.arr.append(hex)
                        self.parent.add_widget(hex)
            # set pressed
            self.pressed = True
            return

    def valid(self, unit, y, x):
        """
        function that validates the location where unit can go
        :param unit: self
        :param y: int y coordinate
        :param x: int x coordinate
        :return: True if all condition are false, else return False
        """

        if locations[y][x] == 'm': # check if location is mountain
            return False

        if locations[y][x] == 'w' and type(unit) != Empire_Warship: # check if locations is water and unit isnt warship
            return False

        if type(unit) == Empire_Warship and locations[y][x] != 'w' and locations[y][x] != 'p': # check if locations isnt water or water pass and unit is warship
            return False

        for hex in self.parent.children: # check if locations is free from other units
            if type(hex) == Empire_HexTile and hex.loc[0] == y and hex.loc[1] == x and hex.occupied == True and self.parent.parent.parent.empire.state != 'War':
                return False

        # check if location isn't other emprie's tile unless its war or military access
        if (self.parent.parent.parent.e1.tile_arr[y][x] == 'O' or self.parent.parent.parent.e2.tile_arr[y][x] == 'O') and self.parent.parent.parent.empire.state != 'War':
            if self.parent.parent.parent.empire.dip1["military access"] == False and self.parent.parent.parent.empire.dip2["military access"] == False:
                return False
            elif (self.parent.parent.parent.e1.tile_arr[y][x] == 'O' and self.parent.parent.parent.empire.dip1["military access"] == True) or (self.parent.parent.parent.e2.tile_arr[y][x] == 'O' and self.parent.parent.parent.empire.dip3["military access"] == True):
                return True
        # check if nearby tile belongs to an empire we are at war with
        elif self.parent.parent.parent.empire.state == 'War' and ((self.parent.parent.parent.e1.state == 'War' and
                                                                   self.parent.parent.parent.e1.tile_arr[y][x] == 'O') or (
                                                                          self.parent.parent.parent.e2.state == 'War' and
                                                                          self.parent.parent.parent.e2.tile_arr[y][
                                                                              x] == 'O')):
            return True

        return True

    def remove_tiles(self):
        # check if currently unit is pressed to prevent error at removing tiles
        if self.pressed:
            for hex in self.arr:
                self.parent.remove_widget(hex)
            # reset pressed
            self.pressed = False


class Empire_Unit(ToggleButtonBehavior, Image):
    """
        Class Method :
            Mixin ToggleButtonBehavior with Images kivy classes
            The Toggle Button widget acts like a checkbox. When you touch or click it, the state toggles between ‘normal’
            and ‘down’ (as opposed to a Button that is only ‘down’ as long as it is pressed).
            The Empire Unit is the land unit for each empire with the capture territory ability.
    """
    def __init__(self, pos, loc, name, **kwargs):
        """
                Function Method :
                    initialize self and class param
                    ===============================
                    :param pos: pos of the class
                    :param loc: tuple loc of the class
                    :param name: name of parent empire
        """
        super(Empire_Unit, self).__init__(**kwargs)
        self.pos = pos  # pos in the canvas
        self.size = (GetSystemMetrics(0) / POS_Y / 1.3, GetSystemMetrics(1) / POS_X / 1.3)  # size in the canvas
        self.loc = loc  # tuple location on board
        self.name = name  # empire name
        self.score = 0  # score - each unit has personal score value (max 3) which allows it to do certain actions
        self.power = 0  # manpower value - defines unit's strength on the battlfield
        self.pressed = False  # boolean value to check unit is currently pressed
        self.arr = []  # list to contain white hexes for movement
        self.class_name = 'U'  # first letter of class name (for id)
        # configuration for source based on empire
        if name == "Rome":
            self.source = os.path.join('assets', 'images', '54_SPQR.png')
        elif name == "Carthage":
            self.source = os.path.join('assets', 'images', '55_CARTH.png')
        else:
            self.source = os.path.join('assets', 'images', '56_EGY.png')

    def on_state(self, widget, value):
        """
        Triggers on pressing of the Unit
        :param widget: self
        :param value: current state of the Toggle Button
        """
        if value == 'normal':
            # reset opacity
            self.opacity = 1
            # remove all white hexes from board
            self.remove_tiles()

        elif value == 'down':
            # if left clicked on unit
            if self.parent.touch.button == 'left':
                # set new opacity
                self.opacity = 0.5
                # create hexes around the unit where it can go - check their validity with valid()
                if self.loc[1] % 2 == 0:
                    for i in range(self.loc[0], self.loc[0] + 2):
                        for j in range(self.loc[1] - 1, self.loc[1] + 2):
                            if j % 2 == 0:
                                pos = (j * 45, 26 + 50 / 2 + i * 50)
                            else:
                                pos = (j * 45, 26 + i * 50)

                            if (self.loc[0] != i or self.loc[1] != j) and self.valid(self, i, j):
                                hex = Empire_HexTile(pos, (i, j), "white")
                                self.arr.append(hex)
                                self.parent.add_widget(hex)

                    if self.valid(self, self.loc[0] - 1, self.loc[1]):
                        hex = Empire_HexTile((self.loc[1] * 45, 26 + 50 / 2 + (self.loc[0] - 1) * 50),
                                             (self.loc[0] - 1, self.loc[1]), "white")
                        self.arr.append(hex)
                        self.parent.add_widget(hex)

                else:
                    for i in range(self.loc[0] - 1, self.loc[0] + 1):
                        for j in range(self.loc[1] - 1, self.loc[1] + 2):
                            if j % 2 == 0:
                                pos = (j * 45, 26 + 50 / 2 + i * 50)
                            else:
                                pos = (j * 45, 26 + i * 50)

                            if (self.loc[0] != i or self.loc[1] != j) and self.valid(self, i, j) == True:
                                hex = Empire_HexTile(pos, (i, j), "white")
                                self.arr.append(hex)
                                self.parent.add_widget(hex)

                    if self.valid(self, self.loc[0] + 1, self.loc[1]):
                        hex = Empire_HexTile((self.loc[1] * 45, 26 + (self.loc[0] + 1) * 50),
                                             (self.loc[0] - 1, self.loc[1]), "white")
                        self.arr.append(hex)
                        self.parent.add_widget(hex)
            # set pressed
            self.pressed = True
            return

    def valid(self, unit, y, x):
        """
        function that validates the location where unit can go
        :param unit: self
        :param y: int y coordinate
        :param x: int x coordinate
        :return: True if all condition are false, else return False
        """

        if locations[y][x] == 'm':  # check if location is mountain
            return False

        if locations[y][x] == 'w' and type(unit) != Empire_Warship:  # check if locations is water and unit isnt warship
            return False

        if type(unit) == Empire_Warship and locations[y][x] != 'w' and locations[y][
            x] != 'p':  # check if locations isnt water or water pass and unit is warship
            return False

        for hex in self.parent.children:  # check if locations is free from other units
            if type(hex) == Empire_HexTile and hex.loc[0] == y and hex.loc[
                1] == x and hex.occupied == True and self.parent.parent.parent.empire.state != 'War':
                return False

        # check if location isn't other emprie's tile unless its war or military access
        if (self.parent.parent.parent.e1.tile_arr[y][x] == 'O' or self.parent.parent.parent.e2.tile_arr[y][
            x] == 'O') and self.parent.parent.parent.empire.state != 'War':
            if self.parent.parent.parent.empire.dip1["military access"] == False and \
                    self.parent.parent.parent.empire.dip2["military access"] == False:
                return False
            elif (self.parent.parent.parent.e1.tile_arr[y][x] == 'O' and self.parent.parent.parent.empire.dip1[
                "military access"] == True) or (
                    self.parent.parent.parent.e2.tile_arr[y][x] == 'O' and self.parent.parent.parent.empire.dip3[
                "military access"] == True):
                return True
        # check if nearby tile belongs to an empire we are at war with
        elif self.parent.parent.parent.empire.state == 'War' and ((self.parent.parent.parent.e1.state == 'War' and
                                                                   self.parent.parent.parent.e1.tile_arr[y][
                                                                       x] == 'O') or (
                                                                          self.parent.parent.parent.e2.state == 'War' and
                                                                          self.parent.parent.parent.e2.tile_arr[y][
                                                                              x] == 'O')):
            return True

        return True

    def remove_tiles(self):
        # check if currently unit is pressed to prevent error at removing tiles
        if self.pressed:
            for hex in self.arr:
                self.parent.remove_widget(hex)
            # reset pressed
            self.pressed = False


class Empire_Worker(ToggleButtonBehavior, Image):
    """
        Class Method :
            Mixin ToggleButtonBehavior with Images kivy classes
            The Toggle Button widget acts like a checkbox. When you touch or click it, the state toggles between ‘normal’
            and ‘down’ (as opposed to a Button that is only ‘down’ as long as it is pressed).
            The Empire Worker is the land unit for each empire with the farm construction ability.
    """
    def __init__(self, pos, loc, name, **kwargs):
        """
                Function Method :
                    initialize self and class param
                    ===============================
                    :param pos: pos of the class
                    :param loc: tuple loc of the class
                    :param name: name of parent empire
        """
        super(Empire_Worker, self).__init__(**kwargs)
        self.pos = pos  # pos in the canvas
        self.size = (GetSystemMetrics(0) / POS_Y / 1.3, GetSystemMetrics(1) / POS_X / 1.3)  # size in the canvas
        self.loc = loc  # tuple location on board
        self.name = name  # empire name
        self.score = 0  # score - each unit has personal score value (max 3) which allows it to do certain actions
        self.power = 0  # manpower value - defines unit's strength on the battlfield
        self.pressed = False  # boolean value to check unit is currently pressed
        self.arr = []  # list to contain white hexes for movement
        self.class_name = 'W'  # first letter of class name (for id)
        self.source = os.path.join('assets', 'images', 'worker.png') # score of the empire

    def on_state(self, widget, value):
        """
        Triggers on pressing of the Unit
        :param widget: self
        :param value: current state of the Toggle Button
        """
        if value == 'normal':
            # reset opacity
            self.opacity = 1
            # remove all white hexes from board
            self.remove_tiles()

        elif value == 'down':
            # if left clicked on unit
            if self.parent.touch.button == 'left':
                # set new opacity
                self.opacity = 0.5
                # create hexes around the unit where it can go - check their validity with valid()
                if self.loc[1] % 2 == 0:
                    for i in range(self.loc[0], self.loc[0] + 2):
                        for j in range(self.loc[1] - 1, self.loc[1] + 2):
                            if j % 2 == 0:
                                pos = (j * 45, 26 + 50 / 2 + i * 50)
                            else:
                                pos = (j * 45, 26 + i * 50)

                            if (self.loc[0] != i or self.loc[1] != j) and self.valid(self, i, j):
                                hex = Empire_HexTile(pos, (i, j), "white")
                                self.arr.append(hex)
                                self.parent.add_widget(hex)

                    if self.valid(self, self.loc[0] - 1, self.loc[1]):
                        hex = Empire_HexTile((self.loc[1] * 45, 26 + 50 / 2 + (self.loc[0] - 1) * 50),
                                             (self.loc[0] - 1, self.loc[1]), "white")
                        self.arr.append(hex)
                        self.parent.add_widget(hex)

                else:
                    for i in range(self.loc[0] - 1, self.loc[0] + 1):
                        for j in range(self.loc[1] - 1, self.loc[1] + 2):
                            if j % 2 == 0:
                                pos = (j * 45, 26 + 50 / 2 + i * 50)
                            else:
                                pos = (j * 45, 26 + i * 50)

                            if (self.loc[0] != i or self.loc[1] != j) and self.valid(self, i, j) == True:
                                hex = Empire_HexTile(pos, (i, j), "white")
                                self.arr.append(hex)
                                self.parent.add_widget(hex)

                    if self.valid(self, self.loc[0] + 1, self.loc[1]):
                        hex = Empire_HexTile((self.loc[1] * 45, 26 + (self.loc[0] + 1) * 50),
                                             (self.loc[0] - 1, self.loc[1]), "white")
                        self.arr.append(hex)
                        self.parent.add_widget(hex)
            # set pressed
            self.pressed = True
            return

    def valid(self, unit, y, x):
        """
        function that validates the location where unit can go
        :param unit: self
        :param y: int y coordinate
        :param x: int x coordinate
        :return: True if all condition are false, else return False
        """

        if locations[y][x] == 'm':  # check if location is mountain
            return False

        if locations[y][x] == 'w' and type(unit) != Empire_Warship:  # check if locations is water and unit isnt warship
            return False

        if type(unit) == Empire_Warship and locations[y][x] != 'w' and locations[y][
            x] != 'p':  # check if locations isnt water or water pass and unit is warship
            return False

        for hex in self.parent.children:  # check if locations is free from other units
            if type(hex) == Empire_HexTile and hex.loc[0] == y and hex.loc[
                1] == x and hex.occupied == True and self.parent.parent.parent.empire.state != 'War':
                return False

        # check if location isn't other emprie's tile unless its war or military access
        if (self.parent.parent.parent.e1.tile_arr[y][x] == 'O' or self.parent.parent.parent.e2.tile_arr[y][
            x] == 'O') and self.parent.parent.parent.empire.state != 'War':
            if self.parent.parent.parent.empire.dip1["military access"] == False and \
                    self.parent.parent.parent.empire.dip2["military access"] == False:
                return False
            elif (self.parent.parent.parent.e1.tile_arr[y][x] == 'O' and self.parent.parent.parent.empire.dip1[
                "military access"] == True) or (
                    self.parent.parent.parent.e2.tile_arr[y][x] == 'O' and self.parent.parent.parent.empire.dip3[
                "military access"] == True):
                return True
        # check if nearby tile belongs to an empire we are at war with
        elif self.parent.parent.parent.empire.state == 'War' and ((self.parent.parent.parent.e1.state == 'War' and
                                                                   self.parent.parent.parent.e1.tile_arr[y][
                                                                       x] == 'O') or (
                                                                          self.parent.parent.parent.e2.state == 'War' and
                                                                          self.parent.parent.parent.e2.tile_arr[y][
                                                                              x] == 'O')):
            return True

        return True

    def remove_tiles(self):
        # check if currently unit is pressed to prevent error at removing tiles
        if self.pressed:
            for hex in self.arr:
                self.parent.remove_widget(hex)
            # reset pressed
            self.pressed = False

