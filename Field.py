import random
from Case import *


class Field:
    def __init__(self, x, y, nb_mine):
        self.size_x = x
        self.size_y = y
        self.remain = x*y - nb_mine

        self.field = [[Case() for _ in range(self.size_y)] for _ in range(self.size_x)]

        self.define_mine(nb_mine)
        self.define_number()

    def define_mine(self, nb_mine):
        while nb_mine > 0:
            mine_x = random.randint(0, self.size_x-1)
            mine_y = random.randint(0, self.size_y-1)

            if not self.is_there_mine_there(mine_x, mine_y):
                self.get_case(mine_x, mine_y).set_mine()
                nb_mine -= 1

    def is_there_mine_there(self, coord_x, coord_y):
        case = self.get_case(coord_x, coord_y)
        if case is not None:
            return case.has_mine()
        else:
            return False

    def define_number(self):
        for x in range(self.size_x):
            for y in range(self.size_y):
                if not self.is_there_mine_there(x, y):
                    mine_around = 0
                    if self.is_there_mine_there(x-1, y-1):
                        mine_around += 1
                    if self.is_there_mine_there(x-1, y):
                        mine_around += 1
                    if self.is_there_mine_there(x-1, y+1):
                        mine_around += 1
                    if self.is_there_mine_there(x, y-1):
                        mine_around += 1
                    if self.is_there_mine_there(x, y+1):
                        mine_around += 1
                    if self.is_there_mine_there(x+1, y-1):
                        mine_around += 1
                    if self.is_there_mine_there(x+1, y):
                        mine_around += 1
                    if self.is_there_mine_there(x+1, y+1):
                        mine_around += 1

                    self.get_case(x, y).set_value(str(mine_around))

    def get_case(self, coord_x, coord_y):
        if 0 <= coord_x <= self.size_x - 1 and 0 <= coord_y <= self.size_y - 1:
            return self.field[coord_x][coord_y]
        return None

    def is_win(self):
        return self.remain == 0

    def open_case(self, x, y):
        case = self.get_case(x, y)
        if case is not None and not case.is_opened():
            case.open()
            self.remain -= 1
            if case.is_empty():
                for i in (x-1, x, x+1):
                    for j in (y-1, y, y+1):
                        self.open_case(i, j)

    def show_mines(self):
        for i in range(self.size_x):
            for j in range(self.size_y):
                case = self.get_case(i, j)
                if case is not None and case.has_mine():
                    case.open()
