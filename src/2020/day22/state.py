class State:
    def __init__(self, deck_1, deck_2):
        self.deck_1 = deck_1
        self.deck_2 = deck_2

    def __eq__(self, other):
        return self.deck_1 == other.deck_1 \
            and self.deck_2 == other.deck_2
