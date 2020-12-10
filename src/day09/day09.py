def part01(numbers):
    for i in range(25, len(numbers)):
        if not is_sum_of_any_last_25(numbers, i):
            print(numbers[i])


def is_sum_of_any_last_25(numbers, index_current):
    for i in range(index_current-25, index_current):
        for j in range(i, index_current):
            if numbers[i] + numbers[j] == numbers[index_current]:
                return True

    return False


def part02(numbers):
    invalid_number = 1492208709

    index_from = 0
    index_to = 0

    while index_to < len(numbers):
        addition = add_numbers_from_to(numbers, index_from, index_to)
        if addition < invalid_number:
            index_to += 1
        elif addition > invalid_number:
            index_from += 1
        else:
            print(max(numbers[index_from:index_to]) +
                  min(numbers[index_from:index_to]))
            return


def add_numbers_from_to(numbers, index_from, index_to):
    response = 0
    for index in range(index_from, index_to):
        response += numbers[index]
    return response


if __name__ == "__main__":
    with open("resources/input09.txt", "r") as f:
        lines = f.read().splitlines()

    numbers = list(map(int, lines))

    part01(numbers)
    part02(numbers)
