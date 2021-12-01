from functools import reduce


def part1(numbers):
    pairs = [numbers[i:i + 2] for i in range(len(numbers) - 1)]
    result = reduce(lambda a, b: a + (1 if b[0] < b[1] else 0), pairs, 0)
    print(f"Part 1 result: {result}")


def part2(numbers):
    window_pairs = [[numbers[i - 1:i + 2], numbers[i:i + 3]]
                    for i in range(1,
                                   len(numbers) - 2)]
    result = reduce(lambda a, b: a + (1 if sum(b[0]) < sum(b[1]) else 0),
                    window_pairs, 0)
    print(f"Part 2 result: {result}")


if __name__ == "__main__":
    with open("resources/2021/input01.txt", "r") as f:
        lines = f.read().splitlines()

    lines = list(map(int, lines))
    numbers = list(map(int, lines))
    part1(numbers)
    part2(numbers)