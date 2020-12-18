import numpy as np
import itertools


def extend_tensor(tensor):
    extend_tensor = np.zeros(tuple(a + 2 for a in tensor.shape))
    extend_tensor[1:-1, 1:-1, 1:-1] = tensor
    return extend_tensor


def extend_tensor_4d(tensor):
    extend_tensor = np.zeros(tuple(a + 2 for a in tensor.shape))
    extend_tensor[1:-1, 1:-1, 1:-1, 1:-1] = tensor
    return extend_tensor


def part02(lines):

    tensor = np.array([[[list(map(int, list(line))) for line in lines]]])
    tensor = extend_tensor_4d(tensor)

    cells_to_check = set(itertools.product(
        [-1, 0, 1], repeat=4))
    cells_to_check.remove((0, 0, 0, 0))

    for _ in range(6):
        tensor = extend_tensor_4d(tensor)
        new_tensor = np.zeros(tensor.shape)
        for channel in range(1, tensor.shape[0] - 1):
            for row in range(1, tensor.shape[1] - 1):
                for col in range(1, tensor.shape[2] - 1):
                    for sub_col in range(1, tensor.shape[3] - 1):
                        count = 0
                        for cell_to_check in cells_to_check:
                            count += tensor[channel + cell_to_check[0],
                                            row + cell_to_check[1],
                                            col + cell_to_check[2],
                                            sub_col + cell_to_check[3]]

                        if tensor[channel, row, col, sub_col] == 1:
                            if count != 2 and count != 3:
                                new_tensor[channel, row, col, sub_col] = 0
                            else:
                                new_tensor[channel, row, col, sub_col] = 1
                        else:
                            if count == 3:
                                new_tensor[channel, row, col, sub_col] = 1
                            else:
                                new_tensor[channel, row, col, sub_col] = 0

        tensor = new_tensor
    print(tensor.sum())


def part01(lines):
    tensor = np.array([[list(map(int, list(line))) for line in lines]])
    tensor = extend_tensor(tensor)

    cells_to_check = set(itertools.product(
        [-1, 0, 1], repeat=3))
    cells_to_check.remove((0, 0, 0))

    for _ in range(6):
        tensor = extend_tensor(tensor)
        new_tensor = np.zeros(tensor.shape)
        for channel in range(1, tensor.shape[0] - 1):
            for row in range(1, tensor.shape[1] - 1):
                for col in range(1, tensor.shape[2] - 1):
                    count = 0
                    for cell_to_check in cells_to_check:
                        count += tensor[channel + cell_to_check[0],
                                        row + cell_to_check[1], col + cell_to_check[2]]

                    if tensor[channel, row, col] == 1:
                        if count != 2 and count != 3:
                            new_tensor[channel, row, col] = 0
                        else:
                            new_tensor[channel, row, col] = 1
                    else:
                        if count == 3:
                            new_tensor[channel, row, col] = 1
                        else:
                            new_tensor[channel, row, col] = 0

        tensor = new_tensor
    print(tensor.sum())


if __name__ == "__main__":
    with open("resources/input17.txt", "r") as f:
        lines = f.read()

    lines = lines.replace('.', '0')
    lines = lines.replace('#', '1')
    lines = lines.splitlines()
    part01(lines)
    part02(lines)
