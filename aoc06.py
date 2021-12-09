
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
    for day in range(18):
        inc_day(fishes)
        print(f"After {day+1} day has: {len(fishes)} fishes")
        #print(f"x = {(len(fishes)/r0)**(1/(day+1))}")
    #print(len(fishes))
    return len(fishes)

def rotate_fishes(day_fishes):
    #print("bfp", day_fishes)
    new_fish = day_fishes.pop(0)
    #print("ap", day_fishes, "nf", new_fish)
    day_fishes[6] += new_fish
    day_fishes.append(new_fish)


def get_b(fishes):
    day_fishes = [0 for _ in range(9)]
    for fish in fishes:
        day_fishes[fish] += 1
    print("Initial fishes:", day_fishes)

    for day in range(256):
        rotate_fishes(day_fishes)
        print(f"After {day+1} day has: {sum(day_fishes)} fishes")
    print("Final fishes:", day_fishes)
    return sum(day_fishes)

if __name__ == "__main__":
    inputs = get_inputs("inputs/day06")
    test_input = get_inputs("test/test06")
    fishes = inputs
    fishes2 = get_inputs("test/test06")
    print(get_a(fishes2))
    print(get_b(fishes))

    #inputs = get_inputs("inputs/day01")
 