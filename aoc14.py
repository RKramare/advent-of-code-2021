
def get_inputs(path):
    inputs = []
    with open(path, 'r') as file:
        inputs = [line for line in file]
    template = inputs[0].strip()
    inputs = [line.strip().split(" -> ") for line in inputs[2:]]
    rules = {key: value for key, value in inputs}

    return template, rules


def count_ploy(template):
    res = []
    for c in set(template):
        res.append(template.count(c))
    print(max(res)-min(res))

def polymer(template, rules):
    new_template = template[:]
    new_i = 0
    for i in range(len(template) - 1):
        pair = template[i:i+2]
        #print(pair)
        if pair in rules:
            #print(f"first: {new_template[:i+new_i+1]}, pair: {pair}, rule: {rules[pair]}, last: {new_template[i+new_i+1:]}")
            new_template = new_template[:i+new_i+1] + rules[pair] + new_template[i+new_i+1:]
            new_i += 1
            #print(f"iter: {new_template}")
    #print(new_template)
    return new_template


def combine_poly(template, rules):
    for i in range(40):
        print(f"Iteration {i}")
        template = polymer(template, rules)
    count_ploy(template)


if __name__ == "__main__":
    template, rules = get_inputs("inputs/day14")
    #template, rules = get_inputs("test/test14")
    #print(test_input)
    combine_poly(template, rules)


