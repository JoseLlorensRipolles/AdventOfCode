import re


def part01(lines):
    valid_passwords = 0

    for line in lines:
        lower_bound, upper_bound, character, password = extract_parameters(
            line)

        occurences = password.count(character)

        if lower_bound <= occurences <= upper_bound:
            valid_passwords += 1

    print("Solution for part 01: {valid_passwords}".format(
        valid_passwords=valid_passwords))


def part02(lines):
    valid_passwords = 0

    for line in lines:
        first_position, second_position, character, password = extract_parameters(
            line)

        if password[first_position-1] == character or password[second_position-1] == character:
            if password[first_position-1] != password[second_position-1]:
                valid_passwords += 1

    print("Solution for part 02: {valid_passwords}".format(
        valid_passwords=valid_passwords))


def extract_parameters(line):
    search_result = re.search(r'(\d+)-(\d+) (\w): (\w+)', line)
    first_position = int(search_result.group(1))
    second_position = int(search_result.group(2))
    character = search_result.group(3)
    password = search_result.group(4)
    return first_position, second_position, character, password


if __name__ == "__main__":
    with open("resources/2020/input02.txt", "r") as f:
        lines = f.read().splitlines()

    part01(lines)
    part02(lines)
