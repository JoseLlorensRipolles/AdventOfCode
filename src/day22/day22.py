from collections import deque


def build_decks(puzzle_input):
    deck_1 = deque(list(
        map(int, puzzle_input.split('\n\n')[0].splitlines()[1:])))
    deck_2 = deque(list(
        map(int, puzzle_input.split('\n\n')[1].splitlines()[1:])))

    return deck_1, deck_2


if __name__ == "__main__":
    with open("resources/input22.txt", "r") as f:
        puzzle_input = f.read()

    deck_1, deck_2 = build_decks(puzzle_input)
    while deck_1 and deck_2:
        draw_1 = deck_1.popleft()
        draw_2 = deck_2.popleft()

        if draw_1 > draw_2:
            deck_1.append(draw_1)
            deck_1.append(draw_2)
        else:
            deck_2.append(draw_2)
            deck_2.append(draw_1)

    winner_deck = deck_1 if deck_1 else deck_2
    multiplyer = 1
    res = 0
    while winner_deck:
        res += multiplyer*winner_deck.pop()
        multiplyer += 1

    print(res)
