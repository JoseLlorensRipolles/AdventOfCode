import numpy as np
from position import Position


class Tile:

    def __init__(self, tile_text):
        self.id = int(tile_text.splitlines()[0][5:-1])
        self.positions = list()
        self.set_position = None

        current_position = np.array([list(x)
                                     for x in tile_text.splitlines()[1:]])
        for _ in range(4):
            current_position = np.rot90(current_position)
            self.positions.append(Position(current_position))

        current_position = np.flipud(current_position)
        for _ in range(4):
            current_position = np.rot90(current_position)
            self.positions.append(Position(current_position))
