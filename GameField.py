import random

from Cell import Cell
from Color import Color


class GameField:
    def __init__(self, size):
        super().__init__()
        self.field = []
        colors = [Color.RED, Color.BLUE, Color.GREEN]
        for i in range(size):
            self.field.append([])
            for j in range(size*2):
                self.field[i].append(Cell(colors[random.randint(0, 2)]))

