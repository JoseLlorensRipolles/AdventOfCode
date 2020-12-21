import re


def part01(lines):
    accum = 0
    for line in lines:
        a = int(evaluate_part_1(line))
        accum += a

    print(accum)


def find_subexpresion(expression):
    open_parenthesis = 1
    subexpression_end = 1
    while open_parenthesis > 0:
        if expression[subexpression_end] == ")":
            open_parenthesis -= 1
        elif expression[subexpression_end] == "(":
            open_parenthesis += 1
        subexpression_end += 1

    return expression[1: subexpression_end - 1]


def evaluate_part_1(expression):
    index = 0
    if expression[index] == '(':
        subexpression = find_subexpresion(expression)
        accum = evaluate_part_1(subexpression)
        index += len(subexpression)+2
    else:
        accum = int(re.search(r'^(\d)+', expression).group(1))
        index += len(re.search(r'^(\d)+', expression).group(1))

    while index < len(expression):
        opperation = expression[index + 1]
        if opperation == '+':
            if expression[index+3] == '(':
                subexpression = find_subexpresion(
                    expression[index+3:])
                accum += evaluate_part_1(subexpression)
                index += len(subexpression)+2
            else:
                accum += int(re.search(r'^(\d)+',
                                       expression[index + 3:]).group(1))
                index += len(re.search(r'^(\d)+',
                                       expression[index + 3:]).group(1))
        else:
            if expression[index+3] == '(':
                subexpression = find_subexpresion(
                    expression[index+3:])
                accum *= evaluate_part_1(subexpression)
                index += len(subexpression)+2
            else:
                accum *= int(re.search(r'^(\d)+',
                                       expression[index + 3:]).group(1))
                index += len(re.search(r'^(\d)+',
                                       expression[index + 3:]).group(1))

        index += 3

    return accum


if __name__ == "__main__":
    with open("resources/input18.txt", "r") as f:
        lines = f.read().splitlines()

    part01(lines)
