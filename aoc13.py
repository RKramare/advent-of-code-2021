def get_inputs(path):
    x, y, folds = [], [], []
    coords = set()
    switch = False
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not switch:
                inp = tuple(map(int, line.split(",")))
                coords.add(inp)
            elif not line:
                switch = True
            elif switch:
                xy, num = line.split('=')
                inp = [xy[-1], int(num)]
                folds.append(inp)

    return coords, folds


def get_max(coords):
    max_x, max_y = 0, 0
    for coord in coords:
        if coord[0] >= max_x:
            max_x = coord[0]
        if coord[1] >= max_y:
            max_y = coord[1]
    return max_x, max_y


def do_fold(coords: set, fold):
    new_coords = set()

    if fold[0] == 'x':
        fold_x = fold[1]
        for x, y in coords:
            if x > fold_x:
                new_coords.add((2 * fold_x - x, y))
            else:
                new_coords.add((x, y))

    else: # fold == 'y'
        fold_y = fold[1]
        for x, y in coords:
            if y > fold_y:
                new_coords.add((x, 2 * fold_y - y))
            else:
                new_coords.add((x, y))

    return new_coords


def do_folds(coords, folds):
    for fold in folds:
        coords = do_fold(coords, fold)

    max_x, max_y = get_max(coords)
    instruction = [["." for _ in range(max_x+1)] for _ in range(max_y+1)]
    while coords:
        x, y = coords.pop()
        instruction[y][x] = "#"
    for row in instruction:
        str_row = ""
        for col in row:
            str_row += col
        print(str_row)        

if __name__ == "__main__":
    coords, folds = get_inputs("inputs/day13")
    #coords, folds = get_inputs("test/test13")

    do_folds(coords, folds)
