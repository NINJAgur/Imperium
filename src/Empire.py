from src.constants import buildBoard

class Empire:
    def __init__(self, manpower, treasury, capital, name, parent, **kwargs):
        super(Empire, self).__init__(**kwargs)
        self.img = ''
        self.farms = 0
        self.tiles = 1
        self.cities = []
        self.original_tiles = 1
        self.name = name
        self.treasury = treasury
        self.parent_widget = parent
        self.units = []
        self.stability = int(self.farms + self.tiles / 10) - len(self.cities) - len(self.units)
        self.farm_locs = buildBoard(48, 70)
        self.army = 0
        self.workers = 0
        self.ships = 0
        self.capital = capital
        self.manpower = manpower
        self.state = 'Peace'
        self.capital_captured = False
        self.tile_arr = buildBoard(48, 70)
        self.labels = [self.manpower, self.stability, self.treasury]

    def update_titles(self):
        self.labels = [self.manpower, self.stability, self.treasury]

    def update_treasury(self):
        self.treasury = self.treasury + self.tiles * 5 + self.farms * 10 + len(self.cities) * 50
        if self.parent_widget.dip1["trade agreement"]:
            self.treasury = self.treasury + len(self.parent_widget.e1.cities) * 100
        if self.parent_widget.dip3["trade agreement"]:
            self.treasury = self.treasury + len(self.parent_widget.e2.cities) * 100

    def update_manpower(self):
        self.manpower = self.manpower + self.tiles * 10 - len(self.cities) * 100

    def update_stability(self):
        self.stability = int(self.farms + self.tiles / 10) - len(self.cities) - len(self.units)

    def add_locations(self, pos_x, pos_y):
        self.tile_arr[pos_y][pos_x] = 'O'
