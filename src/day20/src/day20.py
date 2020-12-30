from tile import Tile
import numpy as np
import math


def is_corner(position, tiles, tile_id):
    for tile in tiles:
        if tile.id != tile_id:
            for other_position in tile.positions:
                if np.array_equal(position.top, other_position.bot) \
                        or np.array_equal(position.left, other_position.right):
                    return False

    return True


def part01(tiles_text):
    tiles = list()
    for tile_text in tiles_text:
        tiles.append(Tile(tile_text))

    result = 1
    for tile in tiles:
        for position in tile.positions:
            if is_corner(position, tiles, tile.id):
                result *= int(tile.id)
                break

    print(result)


def part02(tiles_text):
    tiles = list()
    for tile_text in tiles_text:
        tiles.append(Tile(tile_text))

    first_corner = None
    for tile in tiles:
        for position in tile.positions:
            if is_corner(position, tiles, tile.id):
                first_corner = tile
                tile.set_position = position
        if first_corner:
            break

    l = int(math.sqrt(len(tiles)))
    tiles_by_id = {tile.id: tile for tile in tiles}
    remaining_tiles = set(tiles)
    remaining_tiles.remove(first_corner)
    puzzle = np.zeros((l, l))
    puzzle[0, 0] = first_corner.id

    for col in range(1, l):
        for tile in remaining_tiles:
            position_on_left = tiles_by_id[puzzle[0, col-1]].set_position
            for position in tile.positions:
                found = False
                if np.array_equal(position_on_left.right, position.left):
                    tile.set_position = position
                    remaining_tiles.remove(tile)
                    puzzle[0, col] = tile.id
                    found = True
                    break
            if found:
                break

    for row in range(1, l):
        for tile in remaining_tiles:
            position_on_top = tiles_by_id[puzzle[row-1, 0]].set_position
            for position in tile.positions:
                found = False
                if np.array_equal(position_on_top.bot, position.top):
                    tile.set_position = position
                    remaining_tiles.remove(tile)
                    puzzle[row, 0] = tile.id
                    found = True
                    break
            if found:
                break

        for col in range(1, l):
            for tile in remaining_tiles:
                position_on_top = tiles_by_id[puzzle[row-1, col]].set_position
                position_on_left = tiles_by_id[puzzle[row, col-1]].set_position
                for position in tile.positions:
                    found = False
                    if np.array_equal(position_on_top.bot, position.top) \
                            and np.array_equal(position_on_left.right, position.left):
                        tile.set_position = position
                        remaining_tiles.remove(tile)
                        puzzle[row, col] = tile.id
                        found = True
                        break
                if found:
                    break
    print(puzzle)


if __name__ == "__main__":
    with open("resources/input20.txt", "r") as f:
        tiles_text = f.read().split('\n\n')

    # part01(tiles_text)
    part02(tiles_text)
