
def get_inputs(path):
    inputs = []
    with open(path, 'r') as file:
        inputs =  [line.strip() for line in file]
    return inputs


def mirror(c):
    if c == ")":
        return "("
    if c == "]":
        return "["
    if c == "}":
        return "{"
    if c == ">":
        return "<"
    if c == "(":
        return ")"
    if c == "[":
        return "]"
    if c == "{":
        return "}"
    if c == "<":
        return ">"


VALUE_DICT = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

VALUE_DICT2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def get_a(errors):
    count = 0
    illegal = []
    incompletes = []
    for error in errors:
        incomplete = True
        opened = []
        for c in error:
            if not opened:
                opened.append(c)                
            elif c in "([{<":
                opened.append(c)
            elif c in ")]}>":
                if mirror(c) == opened[-1]:
                    opened.pop()
                else:
                    illegal.append(c)
                    opened.pop()
                    incomplete = False
        if incomplete:
            incompletes.append(error)
    for c in illegal:
        count += VALUE_DICT[c]
    return count, incompletes


def get_b(incompletes):
    scores = []
    for line in incompletes:
        opened = []
        
        for c in line:
            if not opened:
                opened.append(c)                
            elif c in "([{<":
                opened.append(c)
            elif c in ")]}>":
                if mirror(c) == opened[-1]:
                    opened.pop()
        res = [mirror(c) for c in opened]
        
        count = 0
        for c in res[::-1]:
            count *= 5
            count += VALUE_DICT2[c]
        scores.append(count)
    scores.sort()
    return scores[len(scores) // 2]


if __name__ == "__main__":
    inputs = get_inputs("inputs/day10")
    test_input = get_inputs("test/test10")
    #print(test_input)
    count, incompletes = get_a(inputs)
    print(count)
    print(get_b(incompletes))
