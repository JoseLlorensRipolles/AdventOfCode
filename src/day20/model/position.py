class Position:
    def __init__(self, position):
        self.top = position[0, :]
        self.bot = position[-1, :]
        self.left = position[:, 0]
        self.right = position[:, -1]
