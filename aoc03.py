def get_inputs(path):
    inputs = []
    with open(path, 'r') as file:
        inputs = [line.strip() for line in file]
    return inputs

def get_a(seq):
    res = [[0, 0] for _ in range(len(seq[0]))]
    #print(res)
    for l in seq:
        for i, c in enumerate(l):
            if c == '0':
                res[i][0] += 1
            else:
                res[i][1] += 1
    
    b_res = ""
    c_res = ""
    for o, i in res:
        
        if o > i:
            b_res = b_res + "0"
            c_res = c_res + "1"
        else:
            b_res = b_res + "1"
            c_res = c_res + "0"
    
    return int(b_res, 2) * int(c_res, 2)


def get_row(seq, row):
    zeros = 0
    ones = 0
    for c in seq:
        if c[row] == '0':
            zeros += 1
        else:
            ones += 1
    return '1' if ones >= zeros else '0'
    

def get_ox(seq):
    row = 0
    while len(seq) > 1:
        res = []
        way = get_row(seq, row)
        #print("seq:", seq, "way;", way)
        for l in seq:
            if l[row] == way:
                res.append(l)
        row += 1
        seq = res
    return seq

def get_co(seq):
    row = 0
    while len(seq) > 1:
        res = []
        way = get_row(seq, row)
        way = '0' if way == '1' else '1'
        #print("seq:", seq, "way;", way)
        for l in seq:
            if l[row] == way:
                res.append(l)
        row += 1
        seq = res
    return seq

def get_b(seq):
    ox = get_ox(seq)
    co = get_co(seq)
    return int(ox[0],2)*int(co[0],2)

if __name__ == "__main__":
    test_input = get_inputs("test/test03")
    input = get_inputs("inputs/day03")

            
    #print(get_a(input))
    print(get_b(input))

    #print(f"Test values: a: horizontal: {horizontal}, depth: {depth}, factor: {horizontal * depth}")
    