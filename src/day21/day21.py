import re
from collections import defaultdict
from functools import reduce
import itertools


def build_alergen_possible_foods(lines):
    alergen_foods = defaultdict(list)
    for line in lines:
        foods = set(line.split('(contains ')[0][:-1].split(" "))
        alergens = line.split('(contains ')[1][:-1].split(", ")
        for alergen in alergens:
            alergen_foods[alergen].append(foods)

    return alergen_foods


def compute_alergen_food(alergen_possible_ingredients):
    alergen_food = dict()
    while len(alergen_possible_ingredients.items()) > 0:
        for key, values in alergen_possible_ingredients.items():
            reduced = reduce(lambda a, b: a.intersection(b), values)
            if len(reduced) == 1:
                food = reduced.pop()
                alergen_food[key] = food
                remove_alergen_and_food(
                    key, food, alergen_possible_ingredients)
                break

    return alergen_food


def remove_alergen_and_food(key, food, alergen_possible_ingredients):
    del alergen_possible_ingredients[key]
    for key, values in alergen_possible_ingredients.items():
        for value in values:
            if food in value:
                value.remove(food)


def both_parts(lines):
    alergen_possible_foods = build_alergen_possible_foods(lines)
    alergen_food = compute_alergen_food(alergen_possible_foods)
    alergic_foods = set(alergen_food.values())
    all_foods = list(itertools.chain(
        *list(map(lambda a: a.split('(contains ')[0][:-1].split(" "), lines))))
    non_alergic_food_count = sum([x not in alergic_foods for x in all_foods])
    print(non_alergic_food_count)
    alergens = list(alergen_food.keys())
    alergens.sort()
    res = ",".join([alergen_food[alergen] for alergen in alergens])
    print(res)


if __name__ == "__main__":
    with open("resources/input21.txt", "r") as f:
        lines = f.read().split('\n')

    both_parts(lines)
