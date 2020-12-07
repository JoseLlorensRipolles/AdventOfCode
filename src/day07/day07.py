import re
from collections import defaultdict


def part01(graph):
    solution = 0
    for bag_type in list(graph.keys()):
        if any([can_cointain_shiny_gold(content_bag_type, graph) for (_, content_bag_type) in graph[bag_type]]):
            solution += 1
    print(solution)


def can_cointain_shiny_gold(bag_type, graph):
    to_visit = [bag_type]
    visited = set()
    while (len(to_visit) != 0):
        bag_type = to_visit.pop()
        if bag_type == "shiny gold":
            return True
        if bag_type not in visited:
            visited.add(bag_type)
            for _, bag_content_type in graph[bag_type]:
                to_visit.append(bag_content_type)
    return False


def part02(graph):
    solution = sum([content_bag_number * number_of_bags(content_bag_type, graph)
                    for (content_bag_number, content_bag_type) in graph['shiny gold']])
    print(solution)


def number_of_bags(bag_type, graph):
    bag_types_to_visit = [bag_type]
    response = 1
    while (len(bag_types_to_visit) != 0):
        bag_type = bag_types_to_visit.pop()
        for bag_content_number, bag_content_type in graph[bag_type]:
            response += bag_content_number * \
                number_of_bags(bag_content_type, graph)
    return response


def build_graph(lines):
    graph = defaultdict(list)
    for line in lines:
        bag_type = re.search(
            r'([a-zA-Z\s]*) bags contain (.*)\.', line).group(1)
        bag_contents = re.search(r'(.*) bags contain (.*)\.', line).group(2)

        for content in bag_contents.split(', '):
            if content != "no other bags":
                content_number = re.search(
                    r'(\d+) ([a-zA-Z\s]*) bag[s]?', content).group(1)
                content_type = re.search(
                    r'(\d+) ([a-zA-Z\s]*) bag[s]?', content).group(2)

                graph[bag_type].append((int(content_number), content_type))
    return graph


if __name__ == "__main__":
    with open("resources/input07.txt", "r") as f:
        lines = f.read().splitlines()

    graph = build_graph(lines)

    part01(graph)
    part02(graph)
