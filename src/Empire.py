"""
Module Empire.py
====================================================================================

This module contains the class Empire
"""

__version__ = '1.0'
__author__ = 'Edan Gurin'

import random

from src.constants import buildBoard


class Empire:
    def __init__(self, manpower, treasury, capital, name, parent, **kwargs):
        super(Empire, self).__init__(**kwargs)
        self.parent_widget = parent  # original parent for empire - MainGame screen
        self.img = ''  # source image for empire
        self.state = 'Peace'  # string value of empire's state - peace / war / defeat
        self.capital_captured = False  # bool value
        self.farms = 0  # number of farms
        self.tiles = 1  # number of tiles
        self.army = 0  # number of units
        self.workers = 0  # number of workers
        self.ships = 0  # number of tiles
        self.original_tiles = 1  # original amount of tiles when first initialized
        self.name = name  # empire name
        self.units = []  # list of empire units
        self.cities = []  # list of cities
        self.rival_empires = None  # rival empires list
        self.capital = capital  # tuple coordinate of capital
        self.dip1 = {"relations": -float("inf"), "non aggression": False, "trade agreement": False,
                     "military access": False, "peace": True, "war": False}  # diplomacy with empire1
        self.dip2 = {"relations": -float("inf"), "non aggression": False, "trade agreement": False,
                     "military access": False, "peace": True, "war": False}  # diplomacy with empire2
        '''
        EMPIRE RESOURCES
        '''
        self.treasury = treasury  # amount of coins empire has to buy units
        self.manpower = manpower  # amount of men empire has to recruit men and add them power
        self.stability = int(self.farms + self.tiles / 10) - len(self.cities) - len(self.units)  # stability

        self.farm_locs = buildBoard(48, 70)  # 2D list of farm locations
        self.tile_arr = buildBoard(48, 70)  # 2D list of empire tile locations
        self.labels = [self.manpower, self.stability, self.treasury]  # labels (for graphic display and updates)

    # update labels
    def update_titles(self):
        self.labels = [self.manpower, self.stability, self.treasury]

    # update treasury + check for trade agreement
    def update_treasury(self):
        self.treasury = self.treasury + self.tiles * 10 + self.farms * 50 + len(self.cities) * 100
        if self.rival_empires is not None:
            if self.dip1["trade agreement"]:
                self.treasury = self.treasury + len(self.rival_empires[0].cities) * 100
            if self.dip2["trade agreement"]:
                self.treasury = self.treasury + len(self.rival_empires[1].cities) * 100

    # update manpower
    def update_manpower(self):
        self.manpower = self.manpower + self.tiles * 50 - len(self.cities) * 100

    # update stability
    def update_stability(self):
        self.stability = int(self.farms + self.tiles / 10) - len(self.cities) - len(self.units)

    # add locations to tile list
    def add_locations(self, pos_x, pos_y):
        self.tile_arr[pos_y][pos_x] = 'O'

    # update diplomacy
    def update_diplomacy(self, empire1, empire2):
        num_tiles1 = 0 # border tiles with empire 1
        num_tiles2 = 0 # border tiles with empire 2
        self.rival_empires = [empire1, empire2]
        for empire in self.rival_empires:
            # run through rival empire's boards
            for i in range(48):
                for j in range(70):
                    if empire.tile_arr[i][j] == 'O':
                        if empire == self.rival_empires[0] and self.parent_widget.check_neighbour(i, j, self) > 0:
                            num_tiles1 += self.parent_widget.check_neighbour(i, j, self)
                        else:
                            num_tiles2 += self.parent_widget.check_neighbour(i, j, self)

        # calculate relations with empire 1 and empire 2
        if self.rival_empires[0].state == 'War' and self.state == 'War':
            self.dip1["relations"] = -100
        else:
            self.dip1["relations"] = num_tiles1 * (-5) + (self.rival_empires[0].army + random.randint(-1, 1)) * 10 + (self.army + random.randint(-1, 1)) * -10
        if self.rival_empires[1].state == 'War' and self.state == 'War':
            self.dip2["relations"] = -100
        else:
            self.dip2["relations"] = num_tiles1 * (-5) + (self.rival_empires[1].army + random.randint(-1, 1)) * 10 + (self.army + random.randint(-1, 1)) * -10


