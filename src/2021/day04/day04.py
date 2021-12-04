import numpy as np
import re


def get_winning_line(cardboard, said_numbers):
    for row in cardboard:
        if all([x in said_numbers for x in row]):
            return row
    for col in cardboard.transpose():
        if all([x in said_numbers for x in col]):
            return col
    return None


def get_sum_unmarked(cardboard, said_numbers):
    total = 0
    for row in cardboard:
        for elem in row:
            if elem not in said_numbers:
                total += elem
    return total


def part1(numbers, cardboards):
    said_numbers = set()
    for number in numbers:
        said_numbers.add(number)
        for cardboard in cardboards:
            winning_line = get_winning_line(cardboard, said_numbers)
            if winning_line is not None:
                sum_unmarked = get_sum_unmarked(cardboard, said_numbers)
                print(f"Part 1 solution: {number * sum_unmarked}")
                return


def part2(numbers, cardboards):
    said_numbers = set()
    winning_cardboards_idx = set()
    for number in numbers:
        said_numbers.add(number)
        for cardboard_idx in range(len(cardboards)):
            cardboard = cardboards[cardboard_idx]
            if cardboard_idx in winning_cardboards_idx:
                continue
            winning_line = get_winning_line(cardboard, said_numbers)
            if winning_line is not None:
                if len(winning_cardboards_idx) == len(cardboards) - 1:
                    sum_unmarked = get_sum_unmarked(cardboard, said_numbers)
                    print(f"Part 2 solution: {number * sum_unmarked}")
                    return
                else:
                    winning_cardboards_idx.add(cardboard_idx)


if __name__ == "__main__":
    with open("resources/2021/input04.txt", "r") as f:
        lines = f.read().splitlines()
        numbers = list(map(int, lines[0].split(",")))
        cardboards = []
        for i in range(2, len(lines) - 2, 6):
            cardboard = list(
                map(lambda x: re.split(r' +', x.strip()), lines[i:i + 5]))
            cardboard = np.array(cardboard, dtype=int)
            cardboards.append(cardboard)
        part1(numbers, cardboards)
        part2(numbers, cardboards)