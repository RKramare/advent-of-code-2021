
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

def get_a(height_map):
    lowpoints = []
    for row in range(len(height_map)):
        for col in range(len(height_map[0])):
            if is_lowpoint(height_map, row, col):
                lowpoints.append(height_map[row][col])
    print(lowpoints)
    return sum([s + 1 for s in lowpoints])
    
if __name__ == "__main__":
    test_input = get_inputs("test/test09")
    inputs = get_inputs("inputs/day09")
    #print(test_input)
    print(get_a(inputs))

    