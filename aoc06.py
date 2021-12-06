
def get_inputs(path):
    inputs = []
    with open(path, 'r') as file:
        inputs = list(map(int, file.readline().split(",")))
    return inputs


def inc_day(fishes):
    for i, fish in enumerate(fishes):
        if fish == 0:
            fishes[i] = 6
            fishes.append(9)
        else:
            fishes[i] -= 1



def get_a(fishes):
    #print(fishes)
    r0 = len(fishes)

    print(r0)
    for day in range(130):
        inc_day(fishes)
        print(f"After {day+1} day has: {len(fishes)} fishes")
        print(f"x = {(len(fishes)/r0)**(1/(day+1))}")
    #print(len(fishes))
    return len(fishes)

import math
def get_b(fishes, days):
    num_fish = len(fishes)



    #return num_fish * ( ** days)

if __name__ == "__main__":
    inputs = get_inputs("inputs/day06")
    test_input = get_inputs("test/test06")
    fishes = test_input
    print(get_a(fishes))
    #print(get_b(fishes, 80))

    #inputs = get_inputs("inputs/day01")
 