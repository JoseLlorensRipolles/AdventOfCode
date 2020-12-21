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


def part01(lines):

    dag, leaves = get_dag(lines)
    while(True):
        for key, value in dag.items():
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
            print('A')
            pass


if __name__ == "__main__":
    with open("resources/input19.txt", "r") as f:
        lines = f.read().splitlines()

    part01(lines)
