from functools import reduce

if __name__ == "__main__":
    with open("resources/2020/input06.txt", "r") as f:
        groups = f.read().split('\n\n')
        groups[-1] = groups[-1].rstrip()

    print(sum(map(lambda x: len(set(list(x.replace('\n', '')))), groups)))
    print(sum(map(lambda x: len(reduce(lambda a, b: set(
        list(a)).intersection(set(list(b))), x.split('\n'))), groups)))
