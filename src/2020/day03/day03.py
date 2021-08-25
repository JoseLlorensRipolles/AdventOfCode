import numpy as np
import functools


def part01(matrix):
    solution = compute_trees(matrix, 3, 1)
    print("Part01 solution: {solution}".format(solution=solution))


def part02(matrix):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    trees = \
        list(
            map(lambda slope:
                compute_trees(
                    matrix, slope[0], slope[1]), slopes))

    solution = functools.reduce(lambda x, y: x*y, trees)

    print("Part02 solution: {solution}".format(solution=solution))


def compute_trees(matrix, right, down):
    tree_counter = 0
    for step in range(int(matrix.shape[0]/down)):
        current_row = step*down
        current_col = (step * right) % matrix.shape[1]
        if matrix[current_row, current_col] == '#':
            tree_counter += 1
    return tree_counter


if __name__ == "__main__":
    with open("resources/2020/input03.txt", "r") as f:
        lines = f.read().splitlines()

    matrix = np.array(list(lines[0]))
    for row in range(1, len(lines)):
        matrix = np.vstack((matrix, np.array(list(lines[row]))))

    part01(matrix)
    part02(matrix)
