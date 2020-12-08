from enum import Enum
import re


class OpCode(Enum):
    NOP = 1
    ACC = 2
    JMP = 3


def part01(program):
    _, accumulator = execute_program(program)
    print(accumulator)


def part02(program):
    ops_to_replace = [OpCode.NOP, OpCode.JMP]
    op_literals = {
        OpCode.NOP: 'nop', OpCode.JMP: 'jmp'}
    op_replacements = {
        OpCode.NOP: 'jmp', OpCode.JMP: 'nop'}

    for op_to_replace in ops_to_replace:
        replacement_index = 0
        while replacement_index != -1:
            replacement_index = get_next_replacement_index(
                program, replacement_index, op_to_replace)

            modified_program = modify_program(
                program, replacement_index, op_literals, op_to_replace, op_replacements)

            check_program(modified_program)


def check_program(modified_program):
    finished_correctly, global_accumulator = execute_program(
        modified_program)
    if finished_correctly:
        print(global_accumulator)
        exit()


def modify_program(program, replacement_index, op_literals, op_to_replace, op_replacements):
    modified_program = program.copy()
    modified_program[replacement_index] = modified_program[replacement_index].replace(
        op_literals[op_to_replace], op_replacements[op_to_replace])
    return modified_program


def get_next_replacement_index(program, last_index_replaced, opertation_code):
    for index in range(last_index_replaced + 1, len(program)):
        op_code, _ = decode_instruction(program[index])
        if op_code == opertation_code:
            return index
    return -1


def execute_program(program):
    pc = 0
    accumulator = 0
    instructions_executed = set()

    while pc not in instructions_executed and pc < len(program):
        instructions_executed.add(pc)
        pc, accumulator = execute_instruction(
            program, pc, accumulator)

    return pc == len(program), accumulator


def decode_instruction(instruction):
    type_literal = re.search(r'(\w{3}) ([+|-]\d+)', instruction).group(1)
    op_code = get_op_code_from_literal(type_literal)

    op_value = int(re.search(r'(\w{3}) ([+|-]\d+)', instruction).group(2))

    return op_code, op_value


def get_op_code_from_literal(op_code_literal):
    if op_code_literal == "nop":
        return OpCode.NOP
    elif op_code_literal == 'acc':
        return OpCode.ACC
    elif op_code_literal == "jmp":
        return OpCode.JMP
    else:
        raise ValueError(
            "Unknown operation literal {}".format(op_code_literal))


def execute_instruction(program, pc, accumulator):
    instruction = program[pc]
    op_code, op_value = decode_instruction(instruction)
    if op_code == OpCode.NOP:
        return pc + 1, accumulator
    elif op_code == OpCode.ACC:
        return pc + 1, accumulator + op_value
    elif op_code == OpCode.JMP:
        return pc + op_value, accumulator
    else:
        raise ValueError("Unknown operation code{}".format(op_code))


if __name__ == "__main__":
    with open("resources/input08.txt", "r") as f:
        program = f.read().splitlines()

    part01(program)
    part02(program)
