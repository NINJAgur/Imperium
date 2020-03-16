from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.image import Image
from src.constants import *
from src.Hexes import *
import os


class Empire_Warship(ToggleButtonBehavior, Image):
    def __init__(self, pos, loc, e1, e2, name, **kwargs):
        super(Empire_Warship, self).__init__(**kwargs)
        self.pos = pos
        self.size = (GetSystemMetrics(0) / POS_Y / 1.3, GetSystemMetrics(1) / POS_X / 1.3)
        self.loc = loc
        self.e1_locs = e1
        self.e2_locs = e2
        self.name = name
        self.score = 0
        self.power = 0
        self.pressed = False
        self.arr = []

        if name == "Rome":
            self.source = os.path.join('assets', 'images', '44_rome_ship.png')
        elif name == "Carthage":
            self.source = os.path.join('assets', 'images', '45_carthage_ship.png')
        else:
            self.source = os.path.join('assets', 'images', '46_egypt_ship.png')

    def on_state(self, widget, value):
        if value == 'normal':
            self.opacity = 1
            self.remove_tiles()

        elif value == 'down':
            if self.parent.touch.button == 'left':
                self.opacity = 0.5
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

            self.pressed = True
            return

    def valid(self, unit, y, x):

        if locations[y][x] == 'm':
            return False

        if locations[y][x] == 'w' and type(unit) != Empire_Warship:
            return False
        elif type(unit) == Empire_Warship and locations[y][x] != 'w' and locations[y][x] != 'p':
            return False

        for hex in self.parent.children:
            if type(hex) == Empire_HexTile and hex.loc[0] == y and hex.loc[
                1] == x and hex.occupied == True and self.parent.parent.parent.empire.state != 'War':
                return False

        if unit.e1_locs[y][x] == 'O' or unit.e2_locs[y][x] == 'O' and self.parent.parent.parent.empire.state != 'War':
            if self.parent.parent.parent.dip1["military access"] == False and self.parent.parent.parent.dip3[
                "military access"] == False:
                return False
            elif (unit.e1_locs[y][x] == 'O' and self.parent.parent.parent.dip1["military access"] == True) or (
                    unit.e2_locs[y][x] == 'O' and self.parent.parent.parent.dip3["military access"] == True):
                return True
        elif self.parent.parent.parent.empire.state == 'War' and ((self.parent.parent.parent.e1.state == 'War' and
                                                                   self.parent.parent.parent.e1.tile_arr[y][
                                                                       x] == 'O') or (
                                                                          self.parent.parent.parent.e2.state == 'War' and
                                                                          self.parent.parent.parent.e2.tile_arr[y][
                                                                              x] == 'O')):
            return True

        return True

    def remove_tiles(self):
        if self.pressed == True:
            for hex in self.arr:
                self.parent.remove_widget(hex)
            self.pressed = False


class Empire_Unit(ToggleButtonBehavior, Image):
    def __init__(self, pos, loc, e1, e2, name, **kwargs):
        super(Empire_Unit, self).__init__(**kwargs)
        self.pos = pos
        self.size = (GetSystemMetrics(0) / POS_Y / 1.3, GetSystemMetrics(1) / POS_X / 1.3)
        self.loc = loc
        self.e1_locs = e1
        self.e2_locs = e2
        self.name = name
        self.score = 0
        self.power = 0
        self.pressed = False
        self.arr = []

        if name == "Rome":
            self.source = os.path.join('assets', 'images', '54_SPQR.png')
        elif name == "Carthage":
            self.source = os.path.join('assets', 'images', '55_CARTH.png')
        else:
            self.source = os.path.join('assets', 'images', '56_EGY.png')

    def on_state(self, widget, value):
        if value == 'normal':
            self.opacity = 1
            self.remove_tiles()

        elif value == 'down':
            if self.parent.touch.button == 'left':
                self.opacity = 0.5
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

            self.pressed = True
            return

    def valid(self, unit, y, x):

        if locations[y][x] == 'm':
            return False

        if locations[y][x] == 'w' and type(unit) != Empire_Warship:
            return False
        elif type(unit) == Empire_Warship and locations[y][x] != 'w':
            return False

        for hex in self.parent.children:
            if type(hex) == Empire_HexTile and hex.loc[0] == y and hex.loc[
                1] == x and hex.occupied == True and self.parent.parent.parent.empire.state != 'War':
                return False

        if unit.e1_locs[y][x] == 'O' or unit.e2_locs[y][x] == 'O' and self.parent.parent.parent.empire.state != 'War':
            if self.parent.parent.parent.dip1["military access"] == False and self.parent.parent.parent.dip3[
                "military access"] == False:
                return False
            elif (unit.e1_locs[y][x] == 'O' and self.parent.parent.parent.dip1["military access"] == True) or (
                    unit.e2_locs[y][x] == 'O' and self.parent.parent.parent.dip3["military access"] == True):
                return True
        elif self.parent.parent.parent.empire.state == 'War' and ((self.parent.parent.parent.e1.state == 'War' and self.parent.parent.parent.e1.tile_arr[y][x] == 'O') or (self.parent.parent.parent.e2.state == 'War' and self.parent.parent.parent.e2.tile_arr[y][x] == 'O')):
            return True

        return True

    def remove_tiles(self):
        if self.pressed == True:
            for hex in self.arr:
                self.parent.remove_widget(hex)
            self.pressed = False


class Empire_Worker(ToggleButtonBehavior, Image):
    def __init__(self, pos, loc, e1, e2, name, **kwargs):
        super(Empire_Worker, self).__init__(**kwargs)
        self.pos = pos
        self.size = (GetSystemMetrics(0) / POS_Y / 1.3, GetSystemMetrics(1) / POS_X / 1.3)
        self.loc = loc
        self.e1_locs = e1
        self.e2_locs = e2
        self.name = name
        self.score = 0
        self.war = False
        self.pressed = False
        self.arr = []
        self.source = os.path.join('assets', 'images', 'worker.png')

    def on_state(self, widget, value):
        if value == 'normal':
            self.opacity = 1
            self.remove_tiles()
            print('normal')

        elif value == 'down':
            if self.parent.touch.button == 'left':
                self.opacity = 0.5
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

            print('down')
            self.pressed = True
            return

    def valid(self, unit, y, x):

        if locations[y][x] == 'm':
            return False

        if locations[y][x] == 'w':
            return False
        elif type(unit) == Empire_Warship and locations[y][x] != 'w':
            return False

        for hex in self.parent.children:
            if type(hex) == Empire_HexTile and hex.loc[0] == y and hex.loc[
                1] == x and hex.occupied == True and self.parent.parent.parent.empire.state != 'War':
                return False

        if unit.e1_locs[y][x] == 'O' or unit.e2_locs[y][x] == 'O' and self.parent.parent.parent.empire.state != 'War':
            if self.parent.parent.parent.dip1["military access"] == False and self.parent.parent.parent.dip3[
                "military access"] == False:
                return False
            elif (unit.e1_locs[y][x] == 'O' and self.parent.parent.parent.dip1["military access"] == True) or (
                    unit.e2_locs[y][x] == 'O' and self.parent.parent.parent.dip3["military access"] == True):
                return True
        elif self.parent.parent.parent.empire.state == 'War' and ((self.parent.parent.parent.e1.state == 'War' and
                                                                   self.parent.parent.parent.e1.tile_arr[y][
                                                                       x] == 'O') or (
                                                                          self.parent.parent.parent.e2.state == 'War' and
                                                                          self.parent.parent.parent.e2.tile_arr[y][
                                                                              x] == 'O')):
            return True

        return True

    def remove_tiles(self):
        if self.pressed == True:
            for hex in self.arr:
                self.parent.remove_widget(hex)
            self.pressed = False