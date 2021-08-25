def find_loop_size(card_public_key):
    subject_number = 7
    value = 1
    max_number = 20201227
    count = 0

    while value != card_public_key:
        value *= subject_number
        value = value % max_number
        count += 1

    return count


def part01(lines):
    card_public_key = int(lines[0])
    door_public_key = int(lines[1])

    card_loop_size = find_loop_size(card_public_key)

    subject_number = door_public_key
    value = 1
    max_number = 20201227

    for _ in range(card_loop_size):
        value *= subject_number
        value = value % max_number

    print(value)


if __name__ == "__main__":
    with open("resources/2020/input25.txt", "r") as f:
        lines = f.read().splitlines()

    part01(lines)
    # This is the last day of AoC and there is only one actual task.
