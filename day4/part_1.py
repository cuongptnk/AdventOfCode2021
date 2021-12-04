def check_board(board, row_index, column_index):
    row_win = True
    for j in range(len(board)):
        if board[row_index][j] != -1:
            row_win = False
    column_win = True
    for i in range(len(board)):
        if board[i][column_index] != -1:
            column_win = False
    return row_win or column_win


def compute_score(board, value):
    total = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != -1:
                total += board[i][j]
    return total * value


# 1. to mark a position: change it's value to -1
# 2. to quickly identify positions to mark: a mapping from value to a list of (board_index, row_index, column_index)
# 3. for a mark position, we only need to check that row and column to see if the board wins
def solution(boards, called, mapping):
    """
    :param boards: list of 5x5 boards
    :param called: list of called numbers
    :param mapping: a mapping from value to a list of (board_index, row_index, column_index)
    :return: score of the first winning board
    """
    for v in called:
        matches = mapping[v]
        for board_index, row_index, column_index in matches:
            boards[board_index][row_index][column_index] = -1
            if check_board(boards[board_index], row_index, column_index):
                return compute_score(boards[board_index], v)
    return -1


if __name__ == "__main__":
    # input_file = 'input_sample.txt'
    input_file = 'input_full.txt'
    boards = []
    mapping = {}
    line_index = 0
    board_index = -1
    with open(input_file, 'r') as f:
        for line in f:
            if line_index == 0:
                called = list(map(int, line.split(',')))
            else:
                line = line.strip()
                if line == '':
                    board_index += 1
                else:
                    line = list(map(int, line.split()))
                    if line_index % 6 == 2:
                        boards.append([line])
                    else:
                        boards[board_index].append(line)
                    for c_index, v in enumerate(line):
                        tuple_v = (board_index, (line_index-2) % 6, c_index)
                        if v not in mapping:
                            mapping[v] = [tuple_v]
                        else:
                            mapping[v].append(tuple_v)
            line_index += 1
    print(solution(boards, called, mapping))








