from functools import reduce


def solve(lines):
    x = 0
    y = 0
    aim = 0
    y2 = 0
    for line in lines:
        command = line[:-2]
        number = int(line[-1])
        if 'forward' == command:
            x += number
            y2 += aim * number
        elif 'up' == command:
            y -= number
            aim -= number
        elif 'down' == command:
            y += number
            aim += number
        else:
            print("Illegal state")
            exit()
    print(f"Part 01 result: {x * y}")
    print(f"Part 02 result: {x * y2}")


if __name__ == "__main__":
    with open("resources/2021/input02.txt", "r") as f:
        lines = f.read().splitlines()
        solve(lines)