import numpy as np


def part01(mat):
    gamma = ''
    epsilon = ''
    rows = len(mat)
    for col in range(mat.shape[1]):
        if np.sum(mat[:, col]) > rows / 2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(f"Part 1 solution: {gamma*epsilon}")


def part02(mat):
    matGenerator = np.copy(mat)
    matScrubber = np.copy(mat)
    for col in range(mat.shape[1]):
        matGenerator = matGenerator[matGenerator[:, col] == int(
            np.sum(matGenerator[:, col]) >= len(matGenerator) / 2)]

        matScrubber = matScrubber[matScrubber[:, col] == int(
            not np.sum(matScrubber[:, col]) >= len(matScrubber) / 2)]

        if matGenerator.shape[0] == 1:
            generatorRating = int(''.join(map(str, matGenerator[0].tolist())),
                                  2)

        if matScrubber.shape[0] == 1:
            scrubberRating = int(''.join(map(str, matScrubber[0].tolist())), 2)

    print(f"Part 2 solution: {generatorRating*scrubberRating}")


if __name__ == "__main__":
    with open("resources/2021/input03.txt", "r") as f:
        lines = list(map(list, f.read().splitlines()))
        mat = np.array(lines, dtype=int)
        part01(mat)
        part02(mat)