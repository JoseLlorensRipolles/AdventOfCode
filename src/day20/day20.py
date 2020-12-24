def part01(tiles):
    print(tiles[0])


if __name__ == "__main__":
    with open("resources/input20.txt", "r") as f:
        tiles = f.read().split('\n\n')

    part01(tiles)
