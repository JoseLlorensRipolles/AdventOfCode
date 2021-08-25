def part01(puzzle_input):
    circle, current_cup = build_circle(puzzle_input, append_to_1M=False)
    circle = play_game(circle, current_cup, num_iterations=100)

    current_cup = 1
    res = []
    for _ in range(len(list(circle.keys())) - 1):
        res.append(str(circle[current_cup]))
        current_cup = circle[current_cup]

    print("".join(res))


def part02(puzzle_input):
    circle, current_cup = build_circle(puzzle_input, append_to_1M=True)
    circle = play_game(circle, current_cup, num_iterations=10_000_000)

    current_cup = 1
    first_number = circle[current_cup]
    second_number = circle[first_number]
    print(first_number * second_number)


def build_circle(numbers, append_to_1M):
    numbers = list(map(int, list(numbers)))
    if append_to_1M:
        for i in range(len(numbers) + 1, 1_000_001):
            numbers.append(i)
    current_cup = numbers[0]
    circle = dict()
    for i in range(len(numbers)):
        circle[numbers[i]] = numbers[(i+1) % len(numbers)]

    return circle, current_cup


def play_game(circle, current_cup, num_iterations):
    min_label = min(list(circle.keys()))
    max_label = max(list(circle.keys()))
    for _ in range(num_iterations):
        pick_up = get_pick_up(circle, current_cup)
        remove_pick_up_from_circle(circle, current_cup,  pick_up)
        destination_cup = get_destination_cup(
            current_cup, pick_up, min_label, max_label)
        circle[pick_up[-1]] = circle[destination_cup]
        circle[destination_cup] = pick_up[0]
        current_cup = circle[current_cup]
    return circle


def get_pick_up(circle, current_cup):
    pick_up = []
    for _ in range(3):
        pick_up.append(circle[current_cup])
        current_cup = circle[current_cup]

    return pick_up


def get_destination_cup(current_cup, pick_up, min_label, max_label):
    destination_cup = current_cup - 1
    while destination_cup in pick_up or destination_cup < min_label:
        destination_cup -= 1
        if destination_cup < min_label:
            destination_cup = max_label

    return destination_cup


def remove_pick_up_from_circle(circle, current_cup, pick_up):
    circle[current_cup] = circle[pick_up[-1]]


if __name__ == "__main__":
    with open("resources/2020/input23.txt", "r") as f:
        puzzle_input = f.read()

    part01(puzzle_input)
    part02(puzzle_input)
