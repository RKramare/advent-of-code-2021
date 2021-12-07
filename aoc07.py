from math import factorial

def get_inputs(path):
    inputs = []
    with open(path, 'r') as file:
        inputs = list(map(int, file.readline().split(",")))
    return inputs


def get_a(crabs):
    priority_crabs = {crab for crab in crabs}
    crab_fuel = {}
    for chosen in priority_crabs:
        fuel = 0
        for crab in crabs:
            fuel += abs(crab - chosen)
        crab_fuel[chosen] = fuel
    
    return min(crab_fuel.values())
    

def get_sum(n):
    res = 0
    for i in range(1, n + 1):
        res += i
    return res


def get_b(crabs):
    min_crab, max_crab = min(crabs), max(crabs) + 1
    crab_fuel = {}
    for chosen in range(min_crab, max_crab):
        fuel = 0
        for crab in crabs:
            cost = get_sum(abs(crab - chosen))
            fuel += cost
        crab_fuel[chosen] = fuel
    
    return min(crab_fuel.values())


if __name__ == "__main__":
    crabs = get_inputs("inputs/day07")
    test_crabs = get_inputs("test/test07")

    print(get_a(crabs))
    print(get_b(crabs))
