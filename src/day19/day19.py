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


def get_valid_messages(dag, leaves, is_part02=False):
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

        if is_part02:
            rule_42 = ""
            rule_31 = ""
            if '42' in leaves:
                a = ['(']
                for pattern in dag['42']:
                    a += pattern
                    a += ['|']
                a = a[:-1]
                a += [')']
                rule_42 = a

            if '31' in leaves:
                a = ['(']
                for pattern in dag['31']:
                    a += pattern
                    a += ['|']
                a = a[:-1]
                a += [')']
                rule_31 = a

            if '31' in leaves and '42' in leaves:
                return ''.join(rule_42), ''.join(rule_31)


def is_leaf(key, dag):
    patterns = dag[key]
    is_alpha = True
    leaf_characters = r"^[ab\+\(\)\|]*$"
    for pattern in patterns:
        is_alpha = is_alpha and re.compile(
            leaf_characters).match("".join(pattern))
    return is_alpha


def count_valid_msg(rules, messages, is_part02=False):

    res = 0
    dag, leaves = get_dag(rules)
    valid_messages = get_valid_messages(dag, leaves, is_part02=is_part02)
    print(len(valid_messages))
    for message in messages:
        for valid_message in valid_messages:
            valid_message = '^'+valid_message+"$"
            match = re.match(valid_message, message)
            if match != None:
                res += 1
                break

    print(res)


def part02(rules, messages):
    res = 0
    dag, leaves = get_dag(rules)
    rule_42, rule_31 = get_valid_messages(dag, leaves, is_part02=True)
    for message in messages:
        rule_42_count = 0
        match = re.search('^'+rule_42, message)
        while match is not None:
            message = re.sub('^'+rule_42, '', message)
            match = re.search('^'+rule_42, message)
            rule_42_count += 1

        rule_31_count = 0
        match = re.search('^'+rule_31, message)
        while match is not None:
            message = re.sub('^'+rule_31, '', message)
            match = re.search('^'+rule_31, message)
            rule_31_count += 1

        if message == '' and rule_42_count > rule_31_count and rule_31_count > 0:
            res += 1

    print(res)


if __name__ == "__main__":
    with open("resources/input19.txt", "r") as f:
        puzzle_input = f.read().split('\n\n')

    rules = puzzle_input[0].splitlines()
    messages = puzzle_input[1].splitlines()

    # count_valid_msg(rules, messages)
    part02(rules, messages)
