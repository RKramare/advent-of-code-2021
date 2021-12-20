from ast import literal_eval

def get_list(num, depth=0):
    if not num:
        return []
    if isinstance(num[0], list):
        return get_list(num[0], depth + 1) + get_list(num[1:], depth)
    else:
        return [(num[0], depth)] + get_list(num[1:], depth)


def get_inputs(path):
    homework = []
    with open(path, 'r') as file:
        homework = [literal_eval(line.strip()) for line in file]
    return homework


def addition(num1, num2):
    res = num1 + num2
    return [(num, depth + 1) for num, depth in res]


def split(num, depth):
    left = num // 2
    right = num // 2 if num % 2 == 0 else num // 2 + 1
    return (left, depth + 1), (right, depth + 1)


def valid_num(res):
    for num, depth in res:
        if num > 9 or depth == 4:
            return False
    return True


def explode(res):
    new_res = []
    tmp_add = None
    exp = False
    for i in range(len(res)):
        if exp:
            exp = False
            continue
        num1, depth1 = res[i]
        if depth1 == 4:
            num2, _ = res[i + 1]
            if new_res:
                prev_num, prev_depth = new_res[-1]
                if tmp_add:
                    new_res[-1] = (prev_num + num1 + tmp_add, prev_depth)
                    tmp_add = None
                else:
                    new_res[-1] = (prev_num + num1, prev_depth)
            tmp_add = num2
            new_res.append((0, depth1 - 1))
            exp = True
        else:
            if tmp_add:
                new_res.append((num1 + tmp_add, depth1))
                tmp_add = None
            else:
                new_res.append((num1, depth1))

    return new_res


def reduce(res):
    while not valid_num(res):
        res = explode(res)
        for i, val in enumerate(res):
            num, depth = val
            if num > 9:
                first, second = split(num, depth)
                res.pop(i)
                res.insert(i, first)
                res.insert(i + 1, second)
                break
            
    return res

 
def get_magnitude(res):
    i = 0
    while True:
        if len(res) == 1:
            return res[0][0]

        num1, depth1 = res[i]
        num2, depth2 = res[i + 1]
        if depth1 == depth2:
            res.pop(i)
            res.pop(i)
            res.insert(i, (num1 * 3 + num2 * 2, depth1 - 1))
            i = 0
        else:
            i += 1


def do_homework(homework):
    res = get_list(homework[0])
    for i in range(1, len(homework)):
        num = get_list(homework[i])
        res = addition(res, num)
        res = reduce(res)
    print(res)
    return get_magnitude(res)


def find_largest(homework):
    max_mag = 0
    for i in range(len(homework)):
        for j in range(len(homework)):
            if i == j:
                continue
            res1 = get_list(homework[i])
            res2 = get_list(homework[j])
            res = addition(res1, res2)
            res = reduce(res)
            mag = get_magnitude(res)
            if mag > max_mag:
                max_mag = mag
    return max_mag


if __name__ == "__main__":
    homework = get_inputs("inputs/day18")
    # homework = get_inputs("test/test18")

    print("Homework part 1:", do_homework(homework))
    print("Homework part 2:", find_largest(homework))
