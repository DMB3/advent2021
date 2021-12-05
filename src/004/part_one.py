import common


def board_won(board):
    # has any row won?
    for row in board:
        all_none = all(element is None for element in row)
        if all_none:
            return True

    # has any column won?
    for x in range(len(board[0])):
        all_none = True
        for y in range(len(board)):
            if board[y][x] is not None:
                all_none = False
                break

        if all_none:
            return True

    return False


def find_winner(boards):
    for board in boards:
        if board_won(board):
            return board

    return None


def hit_number(number, boards):
    new_boards = []
    for board in boards:
        new_board = []
        for row in board:
            new_row = [element if element != number else None for element in row]
            new_board.append(new_row)
        board = new_board
        new_boards.append(board)

    return new_boards, find_winner(new_boards)


if __name__ == "__main__":
    for input_file in common.inputs:
        lines = list(common.read_file(input_file))
        bingo_input = lines[0].strip()

        boards = []
        current_board = []
        for line_input in lines[1:]:
            line_input = line_input.strip()

            if not line_input:
                if len(current_board) > 0:
                    boards.append(current_board)
                current_board = []
            else:
                pieces = []
                for part in line_input.split(" "):
                    if part:
                        pieces.append(int(part))
                current_board.append(pieces)

        boards.append(current_board)

        winner = None
        drawn = None
        for drawn in bingo_input.split(","):
            boards, winner = hit_number(int(drawn), boards)
            if winner is not None:
                break

        winner_sum = 0
        for row in winner:
            for value in row:
                winner_sum += int(value) if value is not None else 0

        print(f"The bingo winner result is {winner_sum * int(drawn)} for {input_file}!")
