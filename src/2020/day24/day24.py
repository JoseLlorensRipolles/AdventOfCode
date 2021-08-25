import re
from navigation_hexa_grid import *
import numpy as np


def part01(lines):
    floor = build_floor(lines)

    print(np.sum(floor))


def part02(lines):
    floor = build_floor(lines)
    for _ in range(100):
        floor = next_day(floor)

    print(np.sum(floor))


def build_floor(lines):
    # The number of iterations is small enough that we can just create a 200x200 board and there is no need to expand it.
    # Were the number of iterations bigger, we should control board expansion
    matrix = np.zeros((200, 200), dtype=bool)
    offset = 100
    for line in lines:
        movements = parse_line(line)
        final_coordinates = execute_movements(movements)
        x, y = final_coordinates
        x += offset
        y += offset
        matrix[x, y] = not matrix[x, y]
    return matrix


def parse_line(line):
    movements = []
    while len(line) > 0:
        movement = re.search(r'^(e|se|sw|w|nw|ne).*', line).group(1)
        movements.append(movement)
        line = line[len(movement):]
    return movements


def execute_movements(movements):
    current_coord = (0, 0)
    for movement in movements:
        if movement == 'w':
            current_coord = get_w(current_coord)
        elif movement == 'nw':
            current_coord = get_nw(current_coord)
        elif movement == 'ne':
            current_coord = get_ne(current_coord)
        elif movement == 'e':
            current_coord = get_e(current_coord)
        elif movement == 'se':
            current_coord = get_se(current_coord)
        elif movement == 'sw':
            current_coord = get_sw(current_coord)
        else:
            raise Exception(f"No known movment: {movement}")
    return current_coord


def next_day(floor):
    next_day_floor = np.copy(floor)
    for row in range(2, floor.shape[0]-2):
        for col in range(2, floor.shape[1]-2):
            count = 0
            adjacents_functions = [get_w, get_nw,
                                   get_ne, get_e, get_se, get_sw]
            for function in adjacents_functions:
                x, y = function((row, col))
                if floor[x, y]:
                    count += 1

            if floor[row, col] and (count == 0 or count > 2):
                next_day_floor[row, col] = False

            if not floor[row, col] and count == 2:
                next_day_floor[row, col] = True

    return next_day_floor


if __name__ == "__main__":
    with open("resources/2020/input24.txt", "r") as f:
        lines = f.read().splitlines()

    part01(lines)
    part02(lines)
