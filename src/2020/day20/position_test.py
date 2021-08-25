import unittest
from position import Position
import numpy as np


class PositionTest(unittest.TestCase):
    def test_builder(self):
        position = Position(np.array([[1, 2], [3, 4]]))

        np.testing.assert_equal(position.top, [1, 2])
        np.testing.assert_equal(position.bot, [3, 4])
        np.testing.assert_equal(position.left, [1, 3])
        np.testing.assert_equal(position.right, [2, 4])

    def test_equals(self):
        position1 = Position(np.array([[1, 2], [3, 4]]))
        position2 = Position(np.array([[1, 2], [3, 4]]))
        self.assertEqual(position1, position2)

        position1 = Position(np.array([[1, 2], [3, 4]]))
        position2 = Position(np.array([[1, 7], [3, 4]]))
        self.assertNotEquals(position1, position2)

        position1 = Position(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        position2 = Position(np.array([[1, 2, 3], [4, 99, 6], [7, 8, 9]]))
        self.assertEqual(position1, position2)


if __name__ == "__main__":
    unittest.main()
