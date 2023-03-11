from Color import Color

cell_size = 40


class Cell:
    color = None

    def __init__(self, color=Color.RED):
        super().__init__()
        self.size = cell_size
        self.color = color
