import random

from Cell import Cell
from Color import Color


class GameField:
    def __init__(self, size, colors_size):
        super().__init__()
        self.field = []
        colors = [Color.RED, Color.BLUE, Color.GREEN, Color.PURPLE, Color.YELLOW]
        for i in range(size):
            self.field.append([])
            for j in range(size*2):
                self.field[i].append(Cell(colors[random.randint(0, colors_size - 1)]))

