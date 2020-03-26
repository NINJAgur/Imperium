"""
Module constants.py
============

This module contains all the constants used by the other modules of the project
"""

__version__ = '1.0'
__author__ = 'Edan Gurin'

'''
Python imports
'''
from win32api import GetSystemMetrics
from math import inf

MAX, MIN = inf, -inf  # constants max, min for Minimax algorithm

'''------------------------------------------------------------------------------------------------------------------'''


def buildBoard(x, y):  # function that creates a board with 1 values and returns it
    """
    :param x - horizontal length
    :param y - vertical length
    :return: created board
    """
    board = []
    for i in range(x):
        board_row = []
        for j in range(y):
            board_row.append(1)
        board.append(board_row)
    return board


'''------------------------------------------------------------------------------------------------------------------'''

locations = buildBoard(48, 70)  # terrain map constant

"""
COLOURS FOR PIXEL READING

"""
blue = [0.6, 0.8, 1.0, 1.0]  # SEA RGBA VALUE
green = [0.9058823529411765, 0.9686274509803922, 0.611764705882353, 1.0]  # GRASSLANDS RGBA VALUE
yellow = [1, 0.97254901960784313725490196078431, 0.6, 1.0]  # DESERT RGBA VALUE
brown = [0, 0, 0, 1.0]  # MOUNTAINS RGBA VALUE
red = [1, 0, 0, 1.0]  # ROME RGBA VALUE
purple = [0.50196078431372549019607843137255, 0, 1.0, 1.0]  # CARTHAGE RGBA VALUE
yellow2 = [1.0, 1.0, 0, 1.0]  # EGYPT RGBA VALUE
water_pass = [0.54901960784313725490196078431373, 1.0, 0.98431372549019607843137254901961, 1.0]  # WATER PASS RGBA VALUE

'''------------------------------------------------------------------------------------------------------------------'''
'''
POSITION CALCULATION PARAMETERS
'''
dis_height = 48 / 2  # HEIGHT const
dis_width = 43 / 2  # WIDTH  const
POS_Y = GetSystemMetrics(0) / 57.31343283582089552238  # HEIGHT using system height
POS_X = GetSystemMetrics(1) / 60  # WIDTH using system width

# ISLANDS LIST FOR MINIMAX
islands = [(17, 22), (18, 21), (19, 21), (18, 22), (19, 22), (21, 22), (22, 21), (22, 22), (23, 21), (23, 22), (10, 31),
           (15, 49), (11, 47), (10, 48), (11, 49), (10, 50), (11, 51), (13, 61), (13, 62), (12, 62), (14, 63), (13, 63),
           (14, 64)]

'''------------------------------------------------------------------------------------------------------------------'''
