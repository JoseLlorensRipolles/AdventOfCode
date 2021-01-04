import unittest
from navigation_hexa_grid import *


class NavigationHexaGridTest(unittest.TestCase):
    def test_get_w(self):
        current = (1, 0)
        expected = (1, -1)
        outcome = get_w(current)
        self.assertEqual(expected, outcome)

    def test_get_e(self):
        current = (1, 0)
        expected = (1, 1)
        outcome = get_e(current)
        self.assertEqual(expected, outcome)

    def test_get_nw(self):
        current = (1, 2)
        expected = (0, 1)
        outcome = get_nw(current)
        self.assertEqual(expected, outcome)

        current = (2, 2)
        expected = (1, 2)
        outcome = get_nw(current)
        self.assertEqual(expected, outcome)

    def test_get_ne(self):
        current = (1, 2)
        expected = (0, 2)
        outcome = get_ne(current)
        self.assertEqual(expected, outcome)

        current = (2, 2)
        expected = (1, 3)
        outcome = get_ne(current)
        self.assertEqual(expected, outcome)

    def test_get_se(self):
        current = (1, 2)
        expected = (2, 2)
        outcome = get_se(current)
        self.assertEqual(expected, outcome)

        current = (2, 2)
        expected = (3, 3)
        outcome = get_se(current)
        self.assertEqual(expected, outcome)

    def test_get_sw(self):
        current = (1, 2)
        expected = (2, 1)
        outcome = get_sw(current)
        self.assertEqual(expected, outcome)

        current = (2, 2)
        expected = (3, 2)
        outcome = get_sw(current)
        self.assertEqual(expected, outcome)


if __name__ == "__main__":
    unittest.main()
