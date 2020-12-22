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


def get_valid_messages(dag, leaves):
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
                                index = pattern_copy.index(leaf)
                                pattern_copy = pattern_copy[:index] + \
                                    leaf_value+pattern_copy[index+1:]
                                new_values.append(pattern_copy)
                            break
                    if not transformed:
                        new_values.append(pattern)
                dag[key] = new_values

        non_leaves = set(dag.keys()).difference(leaves)
        for key in non_leaves:
            if is_leaf(key, dag):
                leaves.add(key)

        if '0' in leaves:
            return ["".join(a) for a in dag['0']]


def is_leaf(key, dag):
    patterns = dag[key]
    is_alpha = True
    leaf_characters = r"^[ab\*\(\)]*$"
    for pattern in patterns:
        is_alpha = is_alpha and re.compile(
            leaf_characters).match("".join(pattern))
    return is_alpha


def part01(rules, messages):

    res = 0
    dag, leaves = get_dag(rules)
    valid_messages = get_valid_messages(dag, leaves)
    print(len(valid_messages))
    for message in messages:
        for valid_message in valid_messages:
            if message == valid_message:
                res += 1
                break

    print(res)


if __name__ == "__main__":
    with open("resources/input19.txt", "r") as f:
        puzzle_input = f.read().split('\n\n')

    rules = puzzle_input[0].splitlines()
    messages = puzzle_input[1].splitlines()

    part01(rules, messages)
    part02(rules, messages)
