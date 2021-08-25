import math


def part01(lines):
    earliest = int(lines[0])
    current = earliest
    busses = list(map(int, lines[1].replace(r'x,', '').split(',')))
    while True:
        if 0 in [current % x for x in busses]:
            bus_id = busses[[current % x for x in busses].index(0)]
            print(bus_id * (current-earliest))
            return
        current += 1


def part02(lines):
    busses = lines[1].split(',')

    offsets = {}
    for i in range(len(busses)):
        buss = busses[i]
        if buss != 'x':
            offsets[int(buss)] = (int(buss) - i % int(buss))

    busses = [int(x) for x in busses if x != 'x']

    M = math.prod(busses)
    x = 0
    for buss in busses:
        b = int(M/buss)
        b_phi = pow(b, -1, int(buss))
        x += offsets[buss] * b * b_phi

    print(x % M)


if __name__ == "__main__":
    with open("resources/2020/input13.txt", "r") as f:
        lines = f.read().splitlines()

    part01(lines)
    part02(lines)
