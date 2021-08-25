import re


def part01(lines):
    accum = 0
    for line in lines:
        accum += int(evaluate_part_1(line))
    print(accum)


def find_subexpresion_end(expression, sub_expression_start):
    open_parenthesis = 1
    subexpression_end = sub_expression_start + 1
    while open_parenthesis > 0:
        if expression[subexpression_end] == ")":
            open_parenthesis -= 1
        elif expression[subexpression_end] == "(":
            open_parenthesis += 1
        subexpression_end += 1

    return subexpression_end


def evaluate_part_1(expression):

    while "(" in expression:
        sub_expression_start = expression.find('(')
        sub_expression_end = find_subexpresion_end(
            expression, sub_expression_start)
        sub_expression_value = evaluate_part_1(
            expression[sub_expression_start+1:sub_expression_end-1])
        expression = list(expression)
        expression = expression[:sub_expression_start] + \
            [str(sub_expression_value)] + expression[sub_expression_end:]
        expression = "".join(list(expression))

    index = 0
    accum = int(re.search(r'^(\d+)', expression).group(1))
    index += len(re.search(r'^(\d+)', expression).group(1))

    while index < len(expression):
        opperation = expression[index + 1]
        value = re.search(r'^(\d+)', expression[index + 3:]).group(1)
        index += len(value)

        if opperation == '+':
            accum += int(value)
        else:
            accum *= int(value)

        index += 3

    return accum


def part02(lines):
    accum = 0
    for line in lines:
        accum += int(evaluate_part_2(line))
    print(accum)


def evaluate_part_2(expression):

    while "(" in expression:
        sub_expression_start = expression.find('(')
        sub_expression_end = find_subexpresion_end(
            expression, sub_expression_start)
        sub_expression_value = evaluate_part_2(
            expression[sub_expression_start+1:sub_expression_end-1])
        expression = list(expression)
        expression = expression[:sub_expression_start] + \
            [str(sub_expression_value)] + expression[sub_expression_end:]
        expression = "".join(list(expression))

    for operand in ['+', '*']:
        while operand in expression:
            if operand == '+':
                search = re.search(r"((\d+) \+ (\d+))", expression)
            else:
                search = re.search(r"((\d+) \* (\d+))", expression)
            value_a = search.group(2)
            value_b = search.group(3)
            span = search.span()
            if operand == '+':
                result = int(value_a) + int(value_b)
            else:
                result = int(value_a) * int(value_b)

            expression = list(expression)
            expression = expression[:span[0]] + \
                [str(result)] + expression[span[1]:]
            expression = "".join(list(expression))

    return int(expression)


if __name__ == "__main__":
    with open("resources/2020/input18.txt", "r") as f:
        lines = f.read().splitlines()

    part01(lines)
    part02(lines)
