import unittest
from tile import Tile
from position import Position
import numpy as np


class TileTest(unittest.TestCase):
    def test_builder_id(self):
        tile_str = "Tile 2311:\nabc\ndef\nghi"
        tile = Tile(tile_str)
        self.assertEqual(tile.id, 2311)

    def test_builder_positions(self):
        tile_str = "Tile 2311:\nabc\ndef\nghi"
        tile = Tile(tile_str)
        position = Position(
            np.array([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]))
        self.assertTrue(position in tile.positions)

        position = Position(
            np.array([['c', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]))
        self.assertTrue(position not in tile.positions)


if __name__ == "__main__":
    unittest.main()
