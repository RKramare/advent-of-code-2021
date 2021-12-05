
def get_inputs(path):
    inputs = []
    with open(path, 'r') as file:
        inputs = [line.strip().split(" -> ") for line in file]
    res = []
    for i, pair in enumerate(inputs):
        inputs[i] = (tuple(map(int, pair[0].split(","))), tuple(map(int, pair[1].split(","))))
    return inputs


def get_lines(lines):
    hv_lines = []
    dia_lines = []
    for line in lines:
        x1, y1= line[0]
        x2, y2 = line[1]
        if x1 == x2 or y1 == y2:
            hv_lines.append(line)
        else:
            dia_lines.append(line)
    return hv_lines, dia_lines


def find_max(lines):
    max_x = 0
    max_y = 0
    for line in lines:
        x1, y1 = line[0]
        x2, y2 = line[1]
        max_x = max(max_x, max(x1, x2))
        max_y = max(max_y, max(y1, y2))
    return max_x, max_y


def insert_line(grid, line):
    x1, y1 = line[0]
    x2, y2 = line[1]
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    for col in range(x1, x2+1):
        for row in range(y1, y2+ 1):
            grid[row][col] += 1


def insert_dia_line(grid, line):
    x1, y1 = line[0]
    x2, y2 = line[1]
    #x1, x2 = min(x1, x2), max(x1, x2)
    #y1, y2 = min(y1, y2), max(y1, y2)
    if x1 < x2:
        col = [c for c in range(x1, x2+1)]
    else:
        col = [c for c in range(x1, x2-1, -1)]

    if y1 < y2:
        row = [r for r in range(y1, y2+1)]
    else:
        row = [r for r in range(y1, y2-1, -1)]

    for i in range(len(row)):
        grid[row[i]][col[i]] += 1


def create_grid(hv_lines, max_x, max_y, dia_lines=None):
    grid = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]
    for line in hv_lines:
        #print(f"INserting line {line}")
        insert_line(grid, line)
    #print_grid(grid)
    if dia_lines:
        for line in dia_lines:
            #print(f"INserting line {line}")
            insert_dia_line(grid, line)
    return grid


def print_grid(grid):
    for row in grid:
        print(row)


def count_grid(grid):
    count = 0
    for row in grid:
        for col in row:
            if col > 1:
                count += 1
    return count

def get_a(input):
    hv_lines, _ = get_lines(input)
    #print(hv_lines)
    max_x, max_y = find_max(hv_lines)

    #print(max_x, max_y)

    grid = create_grid(hv_lines, max_x, max_y)

    #print_grid(grid)
    return count_grid(grid)



def get_b(input):
    hv_lines, dia_lines = get_lines(input)
    max_x, max_y = find_max(hv_lines)

    #print(max_x, max_y)

    grid = create_grid(hv_lines, max_x, max_y, dia_lines)

    #print_grid(grid)
    return count_grid(grid)


if __name__ == "__main__":
    test_input = get_inputs("test/test05")
    #print(test_input)

    input = get_inputs("inputs/day05")

    print(get_a(input))
    print(get_b(input))
