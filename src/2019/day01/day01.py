from functools import reduce


def part01(module_masses):
    result = reduce(lambda accumulated, update: accumulated +
                    get_fuel_required(update), module_masses, 0)
    print(f"Solution to part 1: {result}")


def part02(module_masses):
    result = reduce(lambda accumulated, update: accumulated +
                    get_fuel_required_with_tyranny(update), module_masses, 0)
    print(f"Solution to part 2: {result}")


def get_fuel_required(mass):
    return max((mass//3) - 2, 0)


def get_fuel_required_with_tyranny(mass):
    current_fuel_required = get_fuel_required(mass)
    fuel_requirements = current_fuel_required
    while(current_fuel_required > 0):
        current_mass = current_fuel_required
        current_fuel_required = get_fuel_required(current_mass)
        fuel_requirements += current_fuel_required
    return fuel_requirements


if __name__ == "__main__":
    with open("resources/2019/input01.txt", "r") as f:
        lines = f.read().splitlines()
        lines = list(map(int, lines))
        part01(lines)
        part02(lines)
