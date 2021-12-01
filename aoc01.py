
def get_inputs(path):
    inputs = []
    with open(path, 'r') as file:
        inputs = list(map(int, [line.strip() for line in file]))
    return inputs


def find_larger(seq):
    prev = float('inf')
    count = 0
    for line in seq:
        if line and int(line) > prev:
            count += 1
        prev = int(line)
        
    return count


def get_three_sum(seq):
    sum_seq = []
    for i in range(0, len(seq)-2):
        sum_seq.append(sum(seq[i:i+3]))
    return sum_seq


if __name__ == "__main__":
    test_input = get_inputs("test/test01")
    test_sum = get_three_sum(test_input)

    print(f"Test values: a: {find_larger(test_input)}. b: {find_larger(test_sum)}.")

    inputs = get_inputs("inputs/day01")
    three_sum = get_three_sum(inputs)

    print(f"Values: a: {find_larger(inputs)}. b: {find_larger(three_sum)}.")
