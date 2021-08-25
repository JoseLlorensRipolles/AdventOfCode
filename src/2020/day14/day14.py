import re
import math


def decode_instruction(instruction):
    mem_dir = int(re.search(r'mem\[(\d+)\] = (\d+)', instruction).group(1))
    value = int(re.search(r'mem\[(\d+)\] = (\d+)', instruction).group(2))

    return mem_dir, value


def decode_mask(instruction):
    return instruction[7:]


def mask_value(mask, value):
    value = value & (int(mask.replace('X', '1'), 2))
    value = value | (int(mask.replace('X', '0'), 2))
    return value


def binary_representation(number, num_bits):
    return bin(number)[2:].zfill(num_bits)


def get_memory_directions(mem_dir, mask):
    memory_directions = []

    mem_dir = mem_dir | (int(mask.replace('X', '0'), 2))
    mem_dir = binary_representation(mem_dir, 36)

    floating_positions = [i for i, x in enumerate(mask) if x == 'X']

    for permutation in get_permutations(num_bits=len(floating_positions)):
        possible_mem_dir = list(mem_dir)
        for j in range(len(floating_positions)):
            floating_value = permutation[j]
            floating_position = floating_positions[j]
            possible_mem_dir[floating_position] = floating_value
        possible_mem_dir = int("".join(possible_mem_dir), 2)
        memory_directions.append(possible_mem_dir)

    return memory_directions


def get_permutations(num_bits):
    return [binary_representation(x, num_bits) for x in range(int(math.pow(2, num_bits)))]


def part01(lines):
    memory = {}
    for instruction in lines:
        if "mask" in instruction:
            mask = decode_mask(instruction)
        else:
            mem_dir, value = decode_instruction(instruction)
            memory[str(mem_dir)] = mask_value(mask, value)

    res = 0
    for _, value in memory.items():
        res += value

    print(res)


def part02(lines):
    memory = {}
    for instruction in lines:
        if "mask" in instruction:
            mask = decode_mask(instruction)
        else:
            mem_dir, value = decode_instruction(instruction)
            memory_directions = get_memory_directions(mem_dir, mask)
            for memory_direction in memory_directions:
                memory[memory_direction] = value

    res = 0
    for _, value in memory.items():
        res += value

    print(res)


if __name__ == "__main__":
    with open("resources/2020/input14.txt", "r") as f:
        lines = f.read().splitlines()

    part01(lines)
    part02(lines)
