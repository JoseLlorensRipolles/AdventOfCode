from collections import deque
from state import State
from copy import deepcopy


def build_decks(puzzle_input):
    deck_1 = deque(list(
        map(int, puzzle_input.split('\n\n')[0].splitlines()[1:])))
    deck_2 = deque(list(
        map(int, puzzle_input.split('\n\n')[1].splitlines()[1:])))

    return deck_1, deck_2


def part01(deck_1, deck_2):
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


def play_recursive_combat(state, is_base_case=False):
    previous_rounds = set()
    deck_1 = state.deck_1
    deck_2 = state.deck_2
    while deck_1 and deck_2:
        hashable_state = (tuple(state.deck_1), tuple(state.deck_2))
        if hashable_state in previous_rounds:
            return 1
        else:
            previous_rounds.add(hashable_state)

        draw_1 = deck_1.popleft()
        draw_2 = deck_2.popleft()

        if len(deck_1) >= draw_1 and len(deck_2) >= draw_2:
            sub_deck_1 = deque(list(deck_1)[0:draw_1])
            sub_deck_2 = deque(list(deck_2)[0:draw_2])
            winner = play_recursive_combat(State(sub_deck_1, sub_deck_2))
        else:
            if draw_1 > draw_2:
                winner = 1
            else:
                winner = 2

        if winner == 1:
            deck_1.append(draw_1)
            deck_1.append(draw_2)
        else:
            deck_2.append(draw_2)
            deck_2.append(draw_1)

    if is_base_case:
        winner_deck = deck_1 if winner == 1 else deck_2
        multiplyer = 1
        res = 0
        while winner_deck:
            res += multiplyer*winner_deck.pop()
            multiplyer += 1
        print(res)
        return

    return 1 if deck_1 else 2


if __name__ == "__main__":
    with open("resources/2020/input22.txt", "r") as f:
        puzzle_input = f.read()

    deck_1, deck_2 = build_decks(puzzle_input)
    part01(deck_1.copy(), deck_2.copy())
    state = State(deck_1, deck_2)
    play_recursive_combat(state, is_base_case=True)
