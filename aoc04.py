
def get_inputs(path):
    inputs = []
    with open(path, 'r') as file:
        inputs = [line.strip() for line in file]

    draws = list(map(int, inputs[0].split(",")))
    boards = []
    board = []
    for line in inputs[1:]:
        if not line:
            if board:
                boards.append(board)
            board = []
        else:
            board.append(list(map(int, line.split())))
    boards.append(board)
        
    print(f"There are {len(boards)} boards and {len(draws)} draws.")
    return draws, boards


def check_bingo(board):
    for row in board:
        if row.count("x") == 5:
            return True
    for col in range(5):
        is_bingo = True
        for row in range(5):
            if not board[row][col] == "x":
                is_bingo = False
                break
        if is_bingo:
            return True
    return False


def set_draw(board, current_draw):
    new_board = []
    new_row = []
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if num == current_draw:
                board[i][j] = "x"
                new_row.append("x")
            else:
                new_row.append(num)
        new_board.append(new_row)


def get_sum(board):
    count = 0
    for row in board:
        for col in row:
            if not col == "x":
                count += col
    return count


def get_a(draws, boards):
    for current_draw in draws:
        for board in boards:
            set_draw(board, current_draw)
            if check_bingo(board):
                print(f"sum: {get_sum(board)}, draw: {current_draw}")
                return get_sum(board) * current_draw
    

def get_b(draws, boards):
    for current_draw in draws:
        to_remove = []
        for i, board in enumerate(boards):
            set_draw(board, current_draw)
            if check_bingo(board):
                if len(boards) > 1:
                    to_remove.append(i)
                else:
                    print(f"sum: {get_sum(board)}, draw: {current_draw}")
                    return get_sum(board) * current_draw
        if to_remove:
            to_remove.sort(reverse=True)
            for i in to_remove:
                boards.pop(i)


if __name__ == "__main__":
    # test_input = get_inputs("test/test04")

    input = get_inputs("inputs/day04")    
    draws, boards = input
    print(f"Final score for a: {get_a(draws, boards)}")

    draws, boards = input
    print(f"Final score for b: {get_b(draws, boards)}")
