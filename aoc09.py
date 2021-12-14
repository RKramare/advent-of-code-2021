
def get_inputs(path):
    inputs = []
    with open(path, 'r') as file:
        inputs =  [list(map(int, list(line.strip()))) for line in file]
    return inputs


def is_in_bounds(height_map, row, col):
    row_max = len(height_map)
    col_max = len(height_map[0])
    return row >= 0 and row < row_max and col >= 0 and col < col_max


def get_point(heigth_map, row, col):
    return int(heigth_map[row][col])


def is_lowpoint(height_map, row, col):
    row_up = row - 1
    row_down = row + 1
    col_left = col - 1
    col_right = col + 1

    #print("r, u, d", row, row_up, row_down)
    #print("c, l, r", col, col_left, col_right)

    current_point = height_map[row][col]# get_point(height_map, row, col)
    #print("Doing:", current_point, row, col)

    if is_in_bounds(height_map, row_up, col):
        if current_point >= height_map[row_up][col]:
            #print("up", current_point, height_map[row_up][col], row_up, col)
            return False

    if is_in_bounds(height_map, row_down, col):
        if current_point >= height_map[row_down][col]:
            #print("down", current_point, height_map[row_down][col], row_down, col)
            return False
    
    if is_in_bounds(height_map, row, col_left):
        if current_point >= height_map[row][col_left]:
            #print("left", current_point, height_map[row][col_left], row, col_left)
            return False
    
    if is_in_bounds(height_map, row, col_right):
        if current_point >= height_map[row][col_right]:
            #print("right", current_point, height_map[row][col_left], row, col_right)
            return False

    #print(f"up {height_map[row_up][col]} down {height_map[row_down][col]} left {height_map[row][col_left]} right {height_map[row][col_right]}")
    #print("Adding:", current_point, row, col)
    
    return True


def is_valid(row, col, height_map, visited):
    return is_in_bounds(height_map, row, col) and \
                not visited[row][col]


def all_visited(visited):
    for row in visited:
        for col in row:
            if not col:
                return False
    return True


def dfs(row, col, height_map, visited):
    if is_valid(row, col, height_map, visited):
        visited[row][col] = True
        if height_map[row][col] == 9:
            return 0
        else:
            sum = 1
            sum += dfs(row-1, col, height_map, visited)
            sum += dfs(row+1, col, height_map, visited)
            sum += dfs(row, col-1, height_map, visited)
            sum += dfs(row, col+1, height_map, visited)
            return sum
    else:
        return 0


def get_b(height_map, low_coords):
    visited = [[False for _ in range(len(height_map[0]))] for _ in range(len(height_map))]
    basin_value = []
    for row, col in low_coords:
        basin_value.append(dfs(row, col, height_map, visited))
    
    #print(basin_value)
    basin_value.sort()
    return basin_value[-1] * basin_value[-2] * basin_value[-3]

def get_a(height_map):
    lowpoints = []
    low_coords = []
    for row in range(len(height_map)):
        for col in range(len(height_map[0])):
            if is_lowpoint(height_map, row, col):
                lowpoints.append(height_map[row][col])
                low_coords.append((row, col))
    #print(lowpoints)
    return sum([s + 1 for s in lowpoints]), low_coords
    
if __name__ == "__main__":
    # height_map = get_inputs("test/test09")
    height_map = get_inputs("inputs/day09")
    #print(test_input)
    a_sum, low_coords = get_a(height_map)
    print(a_sum)
    print(get_b(height_map, low_coords))

    