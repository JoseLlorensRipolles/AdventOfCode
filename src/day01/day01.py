def part01():
    for i in range(0, len(lines)):
        for j in range(i, len(lines)):
            if lines[i] + lines[j] == 2020:
                print("Part1 solution: {solution}".format(
                    solution=lines[i]*lines[j]))
                return


def part02():
    for i in range(0, len(lines)):
        for j in range(i, len(lines)):
            for k in range(j, len(lines)):
                if lines[i] + lines[j] + lines[k] == 2020:
                    print("Part2 solution: {solution}".format(
                        solution=lines[i]*lines[j]*lines[k]))
                    return


if __name__ == "__main__":
    with open("resources/input01.txt", "r") as f:
        lines = f.read().splitlines()

    lines = list(map(int, lines))
    part01()
    part02()
