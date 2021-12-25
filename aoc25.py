from copy import deepcopy as dc

def get_inputs(path):
    with open(path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid


def print_grid(grid):
    for row in grid:
        tmp = ""
        for col in row:
            tmp += col
        print(tmp)


def move_east(grid):
    new_grid = dc(grid)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '>':
                x = col + 1
                if col == len(grid[0]) - 1:
                    x = 0
                if grid[row][x] == '.':
                    new_grid[row][x] = '>'
                    new_grid[row][col] = '.'
    return new_grid


def move_south(grid):
    new_grid = dc(grid)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'v':
                y = row + 1
                if row == len(grid) - 1:
                    y = 0
                if grid[y][col] == '.':
                    new_grid[y][col] = 'v'
                    new_grid[row][col] = '.'
    return new_grid


def get_a(grid):
    moved_grid = dc(grid)
    # print("Before:")
    # print_grid(moved_grid)
    i = 0
    while True:
        orig_grid = dc(moved_grid)
        moved_grid = move_east(moved_grid)
        moved_grid = move_south(moved_grid)
        i += 1
        if orig_grid == moved_grid:
            break
    
    print(f"After {i}")
    # print_grid(moved_grid)




if __name__ == "__main__":
    grid = get_inputs("inputs/day25")
    # grid = get_inputs("test/test25")

    get_a(grid)
