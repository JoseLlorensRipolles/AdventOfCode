
def part01(encoded_seats):

    max_id = 0

    for encoded_seat in encoded_seats:
        row, col = decode_seat(encoded_seat)

        seat_id = row*8+col
        max_id = max(max_id, seat_id)

    print("Part01 solution: {solution}".format(solution=max_id))


def part02(encoded_seats):

    used_seats = list()

    for encoded_seat in encoded_seats:
        row, col = decode_seat(encoded_seat)
        used_seats.append(row*8+col)

    for row in range(0, 127):
        for col in range(7):
            seat_id = row*8+col
            if seat_id not in used_seats and seat_id+1 in used_seats and seat_id - 1 in used_seats:
                print("Part02 solution: {solution}".format(solution=seat_id))


def decode_seat(encoded_seat):
    row = int(encoded_seat[0:7].replace(
        'F', '0').replace('B', '1'), 2)

    col = int(encoded_seat[7:].replace(
        'L', '0').replace('R', '1'), 2)
    return row, col


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    part01(lines)
    part02(lines)
