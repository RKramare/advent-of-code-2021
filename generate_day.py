from os.path import exists


def get_tmp(day):
    return f"""
def get_inputs(path):
    inputs = []
    with open(path, 'r') as file:
        inputs = [line for line in file]
    inputs = [line.strip().split(" -> ") for line in inputs[2:]]

    return inputs


if __name__ == "__main__":
    tmp = get_inputs("inputs/day{day}")
    tmp = get_inputs("test/test{day}")

    print(tmp)

"""


def create_day(day):
    path = "aoc" + str(day) + ".py"
    if not exists(path):
        f = open(path, "w")
        f.write(get_tmp(day))
        f.close()
        d = open("inputs/day" + str(day), "w")
        d.close()
        t = open("test/test" + str(day), "w")
        t.close()
    else:
        print("File exists already")


if __name__ == "__main__":
    create_day(11)
