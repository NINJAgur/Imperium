import os
from kivy.core.image import Image as CoreImage
from src.constants import *
from src.Units import *
from src.constants import buildBoard

dis_height = 48 / 2
dis_width = 43 / 2

background = CoreImage(os.path.join('assets', 'images', 'finalmap.png'))

for i in range(48):
    for j in range(70):
        coor_x = 0
        coor_y = 0
        if j % 2 == 0:
            coor_x = j * dis_width + 10
            coor_y = background.height - dis_height - i * dis_height
        else:
            coor_x = j * dis_width + 10
            coor_y = background.height - dis_height - i * dis_height

        if background.read_pixel(coor_x, coor_y) == green:
            locations[i][j] = 'g'
        elif background.read_pixel(coor_x, coor_y) == yellow:
            locations[i][j] = 'd'
        elif background.read_pixel(coor_x, coor_y) == blue:
            locations[i][j] = 'w'
        elif background.read_pixel(coor_x, coor_y) == brown:
            locations[i][j] = 'm'
        elif background.read_pixel(coor_x, coor_y) == water_pass:
            locations[i][j] = 'p'
        else:
            locations[i][j] = 'c'

def buildMap(empire, empire2, empire3):
    empire_map = buildBoard(48, 70)
    for i in range(48):
        for j in range(70):
            if empire.tile_arr[i][j] == 'O':
                empire_map[i][j] = 'R'
            elif empire2.tile_arr[i][j] == 'O':
                empire_map[i][j] = 'C'
            elif empire3.tile_arr[i][j] == 'O':
                empire_map[i][j] = 'E'
            elif locations[i][j] == 'g':
                empire_map[i][j] = 'g'
            elif locations[i][j] == 'd':
                empire_map[i][j] = 'd'
            elif locations[i][j] == 'w':
                empire_map[i][j] = 'w'
            elif locations[i][j] == 'm':
                empire_map[i][j] = 'm'
            elif locations[i][j] == 'c':
                empire_map[i][j] = 'c'
            else:
                empire_map[i][j] = 'p'

    return empire_map


def units_Map(empire, empire2, empire3):
    unit_map = buildBoard(48, 70)
    for unit in empire.units:
        if type(unit) == Empire_Unit:
            unit_map[unit.loc[0]][unit.loc[1]] = 'RU'
        elif type(unit) == Empire_Worker:
            unit_map[unit.loc[0]][unit.loc[1]] = 'RW'
        elif type(unit) == Empire_Warship:
            unit_map[unit.loc[0]][unit.loc[1]] = 'RS'

    for unit in empire2.units:
        if type(unit) == Empire_Unit:
            unit_map[unit.loc[0]][unit.loc[1]] = 'CU'
        elif type(unit) == Empire_Worker:
            unit_map[unit.loc[0]][unit.loc[1]] = 'CW'
        elif type(unit) == Empire_Warship:
            unit_map[unit.loc[0]][unit.loc[1]] = 'CS'

    for unit in empire3.units:
        if type(unit) == Empire_Unit:
            unit_map[unit.loc[0]][unit.loc[1]] = 'EU'
        elif type(unit) == Empire_Worker:
            unit_map[unit.loc[0]][unit.loc[1]] = 'EW'
        elif type(unit) == Empire_Warship:
            unit_map[unit.loc[0]][unit.loc[1]] = 'ES'

    return unit_map
