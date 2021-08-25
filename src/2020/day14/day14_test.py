import unittest
from day14 import mask_value


class TestDay14(unittest.TestCase):

    def test_mask_value(self):
        mask = "0"
        value = 1
        output = mask_value(mask, value)
        expected = 0
        self.assertEqual(output, expected)

        mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        value = 11
        output = mask_value(mask, value)
        expected = 73
        self.assertEqual(output, expected)

        mask = "0101111110011010X110100010X100000XX0"
        value = 216719
        output = mask_value(mask, value)
        expected = 25663277830
        self.assertEqual(output, expected)

        mask = "01X001X10111X0011X10001100000001X0X1"
        value = 874925389
        output = mask_value(mask, value)
        expected = 19178336281
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
