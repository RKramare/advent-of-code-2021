
def get_inputs(path):
    with open(path, 'r') as file:
        dumbos = [list(map(int, list(line.strip()))) for line in file]
    return dumbos


def flash_dumbo(row, col, dumbos):
    pass


def print_dumbos(dumbos):
    for row in dumbos:
        str_row = ""
        for col in row:
            str_row += str(col)
        print(str_row)   


def increase_energy(dumbos):
    # print("Before:")
    # print_dumbos(dumbos)
    dumbos = [[col + 1 for col in row] for row in dumbos]
    # print("After:")
    # print_dumbos(dumbos)
    for row in range(len(dumbos)):
        for col in range(len(dumbos[0])):
            
            pass
            #dumbos[row][col] += 1
            #flash_dumbo(dumbo)


if __name__ == "__main__":
    dumbos = get_inputs("inputs/day11")
    dumbos = get_inputs("test/test11")

    increase_energy(dumbos)
