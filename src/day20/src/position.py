import numpy as np


class Position:
    def __init__(self, position):
        self.inner_content = position[1:-1, 1:-1]
        self.top = position[0, :]
        self.bot = position[-1, :]
        self.left = position[:, 0]
        self.right = position[:, -1]

    def __eq__(self, other):
        return np.array_equal(self.top, other.top) \
            and np.array_equal(self.bot, other.bot) \
            and np.array_equal(self.left, other.left) \
            and np.array_equal(self.right, other.right)
