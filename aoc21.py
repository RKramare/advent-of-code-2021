
def get_inputs(path):
    with open(path, 'r') as file:
        p1_start = int(file.readline().strip()[-1])
        p2_start = int(file.readline().strip()[-1])

    return p1_start, p2_start


# def move_piece(start, moves):
    

# def throw_die():


def get_a(p1_start, p2_start):
    p1_score = 0
    p2_score = 0
    p1_pos = p1_start
    p2_pos = p2_start
    throw = 1
    rolls = 0
    p1_turn = True
    while p1_score < 1000 and p2_score < 1000:
        dice_sum = 0
        if p1_turn:
            for i in range(throw, throw + 3):
                throw += 1
                dice_sum += i
            p1_pos = (p1_pos + dice_sum) % 10
            p1_pos = 10 if p1_pos == 0 else p1_pos
            p1_score += p1_pos
            p1_turn = False
            # print(f"p1 pos: {p1_pos}, p1 score: {p1_score}")
        else:
            for i in range(throw, throw + 3):
                throw += 1
                dice_sum += i
            p2_pos = (p2_pos + dice_sum) % 10
            p2_score += p2_pos
            p2_pos = 10 if p2_pos == 0 else p2_pos
            p1_turn = True
            # print(f"p2 pos: {p2_pos}, p2 score: {p2_score}")
        # print(f"Dice at: {throw}")
    print(p1_score, p2_score, throw - 1)
    return min(p1_score, p2_score) * (throw - 1)



def get_b(p1_start, p2_start):
    p1_score = 0
    p2_score = 0
    p1_pos = p1_start
    p2_pos = p2_start
    throw = 1
    rolls = 0
    p1_turn = True
    while p1_score < 1000 and p2_score < 1000:
        dice_sum = 0
        if p1_turn:
            for i in range(throw, throw + 3):
                throw += 1
                dice_sum += i
            p1_pos = (p1_pos + dice_sum) % 10
            p1_pos = 10 if p1_pos == 0 else p1_pos
            p1_score += p1_pos
            p1_turn = False
            # print(f"p1 pos: {p1_pos}, p1 score: {p1_score}")
        else:
            for i in range(throw, throw + 3):
                throw += 1
                dice_sum += i
            p2_pos = (p2_pos + dice_sum) % 10
            p2_score += p2_pos
            p2_pos = 10 if p2_pos == 0 else p2_pos
            p1_turn = True
            # print(f"p2 pos: {p2_pos}, p2 score: {p2_score}")
        # print(f"Dice at: {throw}")
    print(p1_score, p2_score, throw - 1)
    return min(p1_score, p2_score) * (throw - 1)



if __name__ == "__main__":
    p1_start, p2_start = get_inputs("inputs/day21")
    # p1_start, p2_start = get_inputs("test/test21")

    print(get_a(p1_start, p2_start))

