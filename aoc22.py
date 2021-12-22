
def get_inputs(path):
    inputs = []
    with open(path, 'r') as file:
        inputs = [line.strip().split(",") for line in file]
    #inputs = [line.strip().split(" -> ") for line in inputs[2:]]
    res = []
    for inp in inputs:
        tmp = [inp[0].split(" ")[0]]
        for c in inp:
            t1, t2 = c.split("..")
            tmp.append((int(t1.split("=")[1]), int(t2)))
        res.append(tmp)
            
    return res


def get_a(inst):
    engine = [[[False for _ in range(-50, 50)] for _ in range(-50, 50)] for _ in range(-50, 50)]
    
    for op, x_i, y_i, z_i in inst:
        op = True if op == 'on' else False
        x_min, x_max = x_i
        y_min, y_max = y_i
        z_min, z_max = z_i
        if abs(x_min) > 50:
            continue
        for z in range(z_min, z_max + 1):
            for y in range(y_min, y_max + 1):
                for x in range(x_min, x_max + 1):
                    engine[z][y][x] = op

    cubes = 0

    for z in engine:
        for y in z:
            cubes += y.count(True)
    
    print(cubes)


if __name__ == "__main__":
    tmp = get_inputs("inputs/day22")
    # tmp = get_inputs("test/test22")

    get_a(tmp)

