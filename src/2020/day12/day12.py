def part01(lines):
    currently_facing = 90
    position = [0, 0]
    direction = {'N': [1, 0], 'S': [-1, 0], 'E': [0, 1], 'W': [0, -1]}

    for line in lines:
        action = line[0]
        value = int(line[1:])

        if action == 'L':
            currently_facing -= value
            currently_facing = currently_facing % 360
        elif action == 'R':
            currently_facing += value
            currently_facing = currently_facing % 360
        elif action == 'F':
            if currently_facing == 0:
                position[0] += value
            elif currently_facing == 180:
                position[0] -= value
            elif currently_facing == 90:
                position[1] += value
            elif currently_facing == 270:
                position[1] -= value
        else:
            position[0] += value * direction[action][0]
            position[1] += value * direction[action][1]

    print(sum(map(abs, position)))


def part02(lines):
    position = [0, 0]
    waypoint = [1, 10]
    direction = {'N': [1, 0], 'S': [-1, 0], 'E': [0, 1], 'W': [0, -1]}
    rotations = {'L': [1, -1], 'R': [-1, 1]}

    for line in lines:
        action = line[0]
        value = int(line[1:])

        if action == 'L' or action == 'R':
            while value > 0:
                waypoint = [waypoint[1] * rotations[action]
                            [0], waypoint[0] * rotations[action][1]]
                value -= 90
        elif action == 'F':
            position[0] += (waypoint[0]*value)
            position[1] += (waypoint[1]*value)
        else:
            waypoint[0] += value * direction[action][0]
            waypoint[1] += value * direction[action][1]

    print(sum(map(abs, position)))


if __name__ == "__main__":
    with open("resources/2020/input12.txt", "r") as f:
        lines = f.read().splitlines()

    part01(lines)
    part02(lines)
