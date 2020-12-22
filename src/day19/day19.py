import re


def get_dag(lines):
    dag = {}
    leaves = set()
    for line in lines:
        key = re.search(r'^(\d+):', line).group(1)
        if '"' in line:
            remainder = re.search(r'^\d+: "(.*)"', line).group(1)
            values = [[remainder]]
            leaves.add(key)
        else:
            remainder = re.search(r'^\d+: (.*)', line).group(1)
            values = [x.split(" ") for x in remainder.split(" | ")]
        dag[key] = values
    return dag, leaves


def part01(rules, messages):

    res = 0
    valid_messages = get_valid_messages(rules)
    print(len(valid_messages))
    for message in messages:
        for valid_message in valid_messages:
            valid = False
            if message == valid_message:
                res += 1
                valid = True
                break

    print(res)


def get_valid_messages(rules):
    dag, leaves = get_dag(rules)
    while(True):
        for key, value in dag.items():
            if key not in leaves:
                new_values = []
                for pattern in value:
                    transformed = False
                    for leaf in leaves:
                        if leaf in pattern:
                            transformed = True
                            for leaf_value in dag[leaf]:
                                pattern_copy = pattern.copy()
                                while leaf in pattern_copy:
                                    index = pattern_copy.index(leaf)
                                    pattern_copy = pattern_copy[:index] + \
                                        leaf_value+pattern_copy[index+1:]
                                new_values.append(pattern_copy)
                            break
                    if not transformed:
                        new_values.append(pattern)
                dag[key] = new_values

        for key, value in dag.items():
            is_alpha = True
            for pattern in value:
                is_alpha = is_alpha and "".join(pattern).isalpha()

            if is_alpha:
                leaves.add(key)

        if '0' in leaves:
            return ["".join(a) for a in dag['0']]


if __name__ == "__main__":
    with open("resources/input19.txt", "r") as f:
        puzzle_input = f.read().split('\n\n')

    rules = puzzle_input[0].splitlines()
    messages = puzzle_input[1].splitlines()

    part01(rules, messages)
