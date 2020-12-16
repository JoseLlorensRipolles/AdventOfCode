from collections import defaultdict


def both_parts(starting_numbers):
    turns_said = defaultdict(list)
    t = 1
    for starting_number in starting_numbers:
        turns_said[starting_number] = [t]
        t += 1

    last_said = starting_numbers[-1]
    while t <= 2020:
        last_said = step(turns_said, last_said, t)
        t += 1
    print(last_said)

    while t <= 30000000:
        last_said = step(turns_said, last_said, t)
        t += 1
    print(last_said)


def step(turns_said, last_said, t):
    if len(turns_said[last_said]) <= 1:
        current_said = 0
    else:
        current_said = turns_said[last_said][0] - turns_said[last_said][1]

    if len(turns_said[current_said]) == 0:
        turns_said[current_said] = [t]
    else:
        turns_said[current_said] = [t, turns_said[current_said][0]]
    last_said = current_said
    return last_said


if __name__ == "__main__":
    with open("resources/input15.txt", "r") as f:
        lines = f.read().splitlines()
    starting_numbers = list(map(int, lines[0].split(',')))
    both_parts(starting_numbers)
