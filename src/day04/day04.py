import re
import itertools
from typing import Optional


def part01(passports):
    solution = 0
    fields_names = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for passport in passports:
        is_valid = all(
            map(lambda x: x in passport, fields_names))
        if is_valid:
            solution += 1

    print("Part01 solution: {solution}".format(solution=solution))


def part02(passports):
    solution = 0

    for passport in passports:
        fields_names = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        is_valid = all(
            map(lambda x: validate_field(x, passport), fields_names))
        if is_valid:
            solution += 1

    print("Part02 solution: {solution}".format(solution=solution))


def validate_field(field_name: str, passport: str):
    field = get_field(field_name, passport)

    if not field:
        return False

    if field_name == "byr":
        return validate_number(field, 1920, 2002, num_digits=4)
    elif field_name == "iyr":
        return validate_number(field, 2010, 2020, num_digits=4)
    elif field_name == 'eyr':
        return validate_number(field, 2020, 2030, num_digits=4)
    elif field_name == 'hgt':
        return validate_height(field)
    elif field_name == 'hcl':
        return validate_hair_color(field)
    elif field_name == 'ecl':
        return validate_eye_color(field)
    elif field_name == 'pid':
        return validate_passport_id(field)
    else:
        raise Exception("Unexpected field_name")


def validate_number(number: str,  min: int, max: int, num_digits=None):

    if not number.isdigit():
        return False

    if num_digits:
        if len(number) != num_digits:
            return False

    return min <= int(number) <= max


def validate_height(height):
    search = re.search(r'(\d+)([c|i][m|n])', height)

    if not search:
        return False

    measurement = search.group(1)
    units = search.group(2)

    return 150 <= int(measurement) <= 193 if units == 'cm' else 59 <= int(measurement) <= 76


def validate_hair_color(hair_color):
    return len(hair_color) == 7 and hair_color[0] == '#' and hair_color[1:].isalnum()


def validate_eye_color(eye_color):
    return eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_passport_id(passport_id):
    return len(passport_id) == 9 and passport_id.isdigit()


def get_field(field, text) -> Optional[str]:

    search = re.search(field+r':(\S*)', text)

    if search:
        return search.group(1)
    else:
        return None


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().split('\n\n')

    passports = list(map(lambda line: line.replace("\n", " "), lines))
    part01(passports)
    part02(passports)
