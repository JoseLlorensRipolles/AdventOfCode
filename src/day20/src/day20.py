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

    tiles_by_id = {tile.id: tile for tile in tiles}
    any_corner = get_any_corner(tiles)
    limit = int(math.sqrt(len(tiles)))-1
    puzzle = assemple_puzzle(tiles, tiles_by_id, any_corner)
    print(int(puzzle[0, 0] * puzzle[limit, 0] *
              puzzle[0, limit] * puzzle[limit, limit]))


def part02(tiles_text):
    tiles = list()
    for tile_text in tiles_text:
        tiles.append(Tile(tile_text))

    tiles_by_id = {tile.id: tile for tile in tiles}
    any_corner = get_any_corner(tiles)
    puzzle = assemple_puzzle(tiles, tiles_by_id, any_corner)
    image = build_image(tiles_by_id, puzzle)
    images = rotate_and_flip_image(image)
    response = compute_roughness(images)
    print(response)


def get_any_corner(tiles):
    first_corner = None
    for tile in tiles:
        for position in tile.positions:
            if is_corner(position, tiles, tile.id):
                first_corner = tile
                tile.set_position = position
        if first_corner:
            break
    return first_corner


def assemple_puzzle(tiles, tiles_by_id, first_corner):
    tiles = tiles_by_id.values()
    l = int(math.sqrt(len(tiles)))

    remaining_tiles = set(tiles)
    remaining_tiles.remove(first_corner)
    puzzle = np.zeros((l, l))
    puzzle[0, 0] = first_corner.id

    for row in range(l):
        for col in range(l):
            for tile in remaining_tiles:
                if row > 0:
                    position_on_top = tiles_by_id[puzzle[row -
                                                         1, col]].set_position
                if col > 0:
                    position_on_left = tiles_by_id[puzzle[row,
                                                          col-1]].set_position
                for position in tile.positions:
                    found = False
                    if (row == 0 or np.array_equal(position_on_top.bot, position.top)) \
                            and (col == 0 or np.array_equal(position_on_left.right, position.left)) \
                            and not (row == 0 and col == 0):
                        tile.set_position = position
                        remaining_tiles.remove(tile)
                        puzzle[row, col] = tile.id
                        found = True
                        break
                if found:
                    break
    return puzzle


def build_image(tiles_by_id, puzzle):
    tiles_per_side = int(math.sqrt(len(tiles_by_id.keys())))
    inner_content_size = tiles_by_id[puzzle[0, 0]
                                     ].set_position.inner_content.shape[0]
    img_side_len = tiles_per_side*inner_content_size
    img = np.full((img_side_len, img_side_len), 'a')
    for row in range(tiles_per_side):
        for col in range(tiles_per_side):
            img[row*inner_content_size:(row+1)*inner_content_size, col*inner_content_size:(
                col+1) * inner_content_size] = tiles_by_id[puzzle[row, col]].set_position.inner_content

    return img


def rotate_and_flip_image(image):
    images = []
    for _ in range(4):
        image = np.rot90(image)
        images.append(image)

    image = np.flipud(image)
    for _ in range(4):
        image = np.rot90(image)
        images.append(image)

    return images


def compute_roughness(images):
    pattern_text = "                  # \n#    ##    ##    ###\n #  #  #  #  #  #   "
    pattern = np.array([list(x) for x in pattern_text.splitlines()])
    pattern_heigh = pattern.shape[0]
    pattern_width = pattern.shape[1]

    image_heigh = images[0].shape[0]
    image_width = images[0].shape[1]

    for image in images:
        is_monster_image = False
        for row in range(image_heigh-pattern_heigh + 1):
            for col in range(image_width - pattern_width + 1):
                is_monster_window = True
                for pattern_row in range(pattern_heigh):
                    for pattern_col in range(pattern_width):
                        if pattern[pattern_row, pattern_col] == "#":
                            if image[row+pattern_row, col+pattern_col] != "#":
                                is_monster_window = False

                if is_monster_window:
                    is_monster_image = True
                    for pattern_row in range(pattern_heigh):
                        for pattern_col in range(pattern_width):
                            if pattern[pattern_row, pattern_col] == "#":
                                image[row+pattern_row, col+pattern_col] = "O"

        if is_monster_image:
            return (image == '#').sum()


if __name__ == "__main__":
    with open("resources/input20.txt", "r") as f:
        tiles_text = f.read().split('\n\n')

    part01(tiles_text)
    part02(tiles_text)
