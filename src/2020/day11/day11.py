import numpy as np


def part01(matrix):
    stable = False
    while not stable:
        stable = True
        new_matrix = matrix.copy()
        for row in range(matrix.shape[0]):
            for col in range(matrix.shape[1]):
                if matrix[row][col] != '.':
                    ocupied_adjacent = get_occupied_adjacent(matrix, row, col)
                    if matrix[row][col] == 'L' and ocupied_adjacent == 0:
                        new_matrix[row][col] = '#'
                        stable = False
                    elif matrix[row][col] == '#' and ocupied_adjacent >= 4:
                        new_matrix[row][col] = 'L'
                        stable = False
        matrix = new_matrix
    print(np.count_nonzero(matrix == '#'))


def part02(matrix):
    stable = False
    while not stable:
        stable = True
        new_matrix = matrix.copy()
        for row in range(matrix.shape[0]):
            for col in range(matrix.shape[1]):
                if matrix[row][col] != '.':
                    ocupied_visible = get_occupied_visible(matrix, row, col)
                    if matrix[row][col] == 'L' and ocupied_visible == 0:
                        new_matrix[row][col] = '#'
                        stable = False
                    elif matrix[row][col] == '#' and ocupied_visible >= 5:
                        new_matrix[row][col] = 'L'
                        stable = False
        matrix = new_matrix
    print(np.count_nonzero(matrix == '#'))


def get_occupied_adjacent(matrix, row, col):

    row_len = matrix.shape[0]
    col_len = matrix.shape[1]

    res = 0

    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                  (1, 0), (1, -1), (0, -1), (-1, -1)]

    for direction in directions:
        if 0 <= row + (direction[0]) < row_len and 0 <= col + (direction[1]) < col_len:
            search_row = row + direction[0]
            search_col = col + direction[1]
            if matrix[search_row][search_col] == '#':
                res += 1

    return res


def get_occupied_visible(matrix, row, col):

    row_len = matrix.shape[0]
    col_len = matrix.shape[1]
    res = 0

    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                  (1, 0), (1, -1), (0, -1), (-1, -1)]

    for direction in directions:
        i = 1
        while 0 <= row + (direction[0] * i) < row_len and 0 <= col + (direction[1] * i) < col_len:
            search_row = row + (direction[0] * i)
            search_col = col + (direction[1] * i)
            if matrix[search_row][search_col] != '.':
                if matrix[search_row][search_col] == '#':
                    res += 1
                break
            i += 1

    return res


if __name__ == "__main__":
    with open("resources/2020/input11.txt", "r") as f:
        lines = f.read().splitlines()

    matrix = np.array([list(line) for line in lines])
    part01(matrix)
    part02(matrix)
