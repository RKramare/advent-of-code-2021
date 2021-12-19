
def get_inputs(path):
    inputs = []
    with open(path, 'r') as file:
        inputs = file.readline().split("..")
    x = int(inputs[0].split("=")[1]), int(inputs[1].split(",")[0])
    y = int(inputs[1].split("=")[1]), int(inputs[2])
    return x, y


def passed_area(x, y, area):
    x_max = area[0][1]
    y_min = area[1][0]
    return x > x_max or y < y_min


def in_area(x, y, area):
    x_min = area[0][0]
    x_max = area[0][1]
    y_min = area[1][0]
    y_max = area[1][1]
    return x >= x_min and x <= x_max and y >= y_min and y <= y_max


def do_steps_a(x, y, area):
    step = 0
    pos_x = 0
    pos_y = 0
    trajectories = []
    while True:
        if in_area(pos_x, pos_y, area):
            return max(trajectories)

        elif passed_area(pos_x, pos_y, area):
            return -1
        else:
            pos_x += x
            pos_y += y

            trajectories.append(pos_y)

            if x < 0:
                x += 1
            elif x > 0:
                x -= 1

            y -= 1
        
        step += 1


def shoot_probe_a(area):
    highest_trajectory = 0
    for x in range(1,300):
        for y in range(-200,500):
            trajectory = do_steps_a(x, y, area)
            if trajectory > highest_trajectory:
                highest_trajectory = trajectory

    print(highest_trajectory)


def do_steps_b(x, y, area):
    pos_x = 0
    pos_y = 0
    while True:
        if in_area(pos_x, pos_y, area):
            return (pos_x, pos_y)

        elif passed_area(pos_x, pos_y, area):
            return None
        else:
            pos_x += x
            pos_y += y

            if x < 0:
                x += 1
            elif x > 0:
                x -= 1

            y -= 1
        

def shoot_probe_b(area):
    distinct = set()
    for x in range(1,300):
        for y in range(-1000,1000):
            trajectory = do_steps_b(x, y, area)
            if trajectory:
                distinct.add((x, y))

    print(len(distinct))



if __name__ == "__main__":
    area = get_inputs("inputs/day17")
    #area = get_inputs("test/test17")

    shoot_probe_a(area)
    shoot_probe_b(area)