def get_inputs(path):
    inputs = []
    with open(path, 'r') as file:
        inputs = [(line.strip("\n").split(" ")[0], int(line.strip("\n").split(" ")[1])) for line in file]
    return inputs


def handle_command(input, horizontal, depth):
    for command, value in input:
        if command == "forward":
            horizontal += value
        if command == "down":
            depth += value
        if command == "up":
            depth -= value
    return horizontal, depth


def handle_aim(input, horizontal, depth, aim):
    for command, value in input:
        if command == "forward":
            horizontal += value
            depth += value * aim
        if command == "down":
            aim += value
        if command == "up":
            aim -= value
    return horizontal, depth


def get_position(input, do_aim=False):
    horizontal = 0
    depth = 0
    if not do_aim:
        return handle_command(input, horizontal, depth)
    else:
        aim = 0
        return handle_aim(input, horizontal, depth, aim)


if __name__ == "__main__":
    test_input = get_inputs("test/test02")

    horizontal, depth = get_position(test_input)
    print(f"Test values: a: horizontal: {horizontal}, depth: {depth}, factor: {horizontal * depth}")
    
    horizontal, depth = get_position(test_input, True)
    print(f"Test values: b: horizontal: {horizontal}, depth: {depth}, factor: {horizontal * depth}")


    input = get_inputs("inputs/day02")

    horizontal, depth = get_position(input)
    print(f"Values: a: horizontal: {horizontal}, depth: {depth}, factor: {horizontal * depth}")

    horizontal, depth = get_position(input, True)
    print(f"Values: b: horizontal: {horizontal}, depth: {depth}, factor: {horizontal * depth}")
