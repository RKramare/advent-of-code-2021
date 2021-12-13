def get_inputs(path):
    x, y, folds = [], [], []
    coords = set()
    switch = False
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            print(line)
            if line and not switch:
                inp = tuple(map(int, line.split(",")))
                coords.add(inp)
                #x.append(inp[0])
                #y.append(inp[1])
            elif not line:
                switch = True
            elif switch:
                inp = [line[-3], int(line[-1])]
                folds.append(inp)

    return coords, folds


def fold(coords, fold):
    max_x = max(x)
    max_y = max(y)
    if fold[0] == 'x':
        pass
    else: # fold == 'y'
        fold_y = fold[1]
        for i, curr_y in enumerate(y):
            if curr_y > fold_y:
                y[i] = 1
    
if __name__ == "__main__":
    #inputs = get_inputs("inputs/day13")
    test_input = get_inputs("test/test13")
    
    print(test_input)
