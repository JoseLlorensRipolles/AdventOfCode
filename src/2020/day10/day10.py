from collections import defaultdict


def part01(joltages):
    joltages.sort()

    one_jumps = 1
    three_jumps = 1

    for i in range(1, len(joltages)):
        if (joltages[i] - joltages[i-1]) == 1:
            one_jumps += 1
        elif (joltages[i] - joltages[i - 1]) == 3:
            three_jumps += 1

    print(one_jumps * three_jumps)


def part02(joltages):
    joltages.sort()
    paths = defaultdict(lambda: 0)
    paths[joltages[-1]] = 1

    for i in range(len(joltages)-2, -1, -1):
        paths[joltages[i]] = sum(
            [paths[joltages[i]+j] for j in range(1, 4)])

    print(sum([paths[joltages[i]] for i in range(3)]))


if __name__ == "__main__":
    with open("resources/2020/input10.txt", "r") as f:
        lines = f.read().splitlines()

    numbers = list(map(int, lines))

    part01(numbers)
    part02(numbers)
