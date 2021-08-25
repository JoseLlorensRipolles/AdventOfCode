import re
import numpy as np
from collections import defaultdict
from functools import reduce


def parse_rule(rule):
    valid_numbers = set()
    rule_name = re.search(r"([a-zA-Z_ ]+):", rule).group(1)
    for number_range in re.findall(r"(\d+-\d+)", rule):
        start = int(re.search(r"(\d+)-(\d+)", number_range).group(1))
        end = int(re.search(r"(\d+)-(\d+)", number_range).group(2))

        for i in range(start, end + 1):
            valid_numbers.add(i)
    return rule_name, valid_numbers


def clean_invalid(rules, nearby_tickets):
    valid_numbers = set()
    for rule in rules:
        _, number_range = parse_rule(rule)
        valid_numbers = valid_numbers.union(number_range)

    valid_tickets = []
    part1_res = 0
    for nearby_ticket in nearby_tickets:
        is_valid = True
        numbers = list(map(int, nearby_ticket.split(',')))
        for number in numbers:
            if number not in valid_numbers:
                part1_res += number
                is_valid = False
                break
        if is_valid:
            valid_tickets.append(numbers)

    return part1_res, valid_tickets


def get_rule_to_col(rule_to_possible_cols):
    rule_to_col = {}
    used_cols = set()
    for i in range(1, 21):
        for rule, values in rule_to_possible_cols.items():
            if len(values) == i:
                col = list(set(values).difference(used_cols))[0]
                rule_to_col[rule] = col
                used_cols.add(col)
    return rule_to_col


def get_rule_to_possible_cols(rule_to_range, matrix):
    rule_to_possible_cols = defaultdict(list)
    for rule, values in rule_to_range.items():
        for col in range(matrix.shape[1]):
            if all(map(lambda x: x in values, matrix[:, col])):
                rule_to_possible_cols[rule].append(col)
    return rule_to_possible_cols


def part02(information):
    rules = information[0].splitlines()
    my_ticket = list(map(int, information[1].splitlines()[1].split(',')))
    nearby_tickets = information[2].splitlines()[1:]

    _, valid_tickets = clean_invalid(rules, nearby_tickets)

    matrix = np.array(valid_tickets)
    rule_to_range = {}
    for rule in rules:
        name, values = parse_rule(rule)
        rule_to_range[name] = values

    rule_to_possible_cols = get_rule_to_possible_cols(rule_to_range, matrix)

    rule_to_col = get_rule_to_col(rule_to_possible_cols)

    res = 1
    for rule, col in rule_to_col.items():
        if "departure" in rule:
            res *= my_ticket[col]

    print(res)


def part01(information):
    rules = information[0].splitlines()
    nearby_tickets = information[2].splitlines()[1:]

    res, _ = clean_invalid(rules, nearby_tickets)

    print(res)


if __name__ == "__main__":
    with open("resources/2020/input16.txt", "r") as f:
        lines = f.read().split('\n\n')
    part01(lines)
    part02(lines)
