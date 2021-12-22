
def get_inputs(path):
    with open(path, 'r') as file:
        dumbos = [list(map(int, list(line.strip()))) for line in file]
    return dumbos



def print_dumbos(dumbos):
    for row in dumbos:
        str_row = ""
        for col in row:
            str_row += str(col)
        print(str_row)   


def in_bounds(dumbos, x, y):
    return x >= 0 and x < len(dumbos[0]) and y >= 0 and y < len(dumbos)


def get_a(dumbos):
    dumbos = [[d + 1 for d in row] for row in dumbos]
    flashed = [[False for _ in row] for row in dumbos]
    again = True
    flashes = 0
    while again:
        again = False
        for row in range(len(dumbos)):
            for col in range(len(dumbos[0])):
                if dumbos[row][col] > 9 and not flashed[row][col]:
                    flashed[row][col] = True
                    flashes += 1
                    for y in range(row - 1, row + 2):
                        for x in range(col - 1, col + 2):
                            if in_bounds(dumbos, x, y):
                                dumbos[y][x] += 1
                    again = True

    for row in range(len(dumbos)):
        for col in range(len(dumbos[0])):
            if flashed[row][col]:
                dumbos[row][col] = 0

    return dumbos, flashes


if __name__ == "__main__":
    dumbos = get_inputs("inputs/day11")
    # dumbos = get_inputs("test/test11")

    flashes = 0
    for i in range(1, 300):
        dumbos, f = get_a(dumbos)
        if f == 100:
            print("turn:", i)
            break
        flashes += f
    print_dumbos(dumbos)
    print(flashes)
