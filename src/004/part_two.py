import common


def remove_winners(boards):
    return_value = []

    for board in boards:
        if board_won(board):
            continue

        return_value.append(board)

    return return_value


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


def find_winner(boards, expected_winners=None, return_winner=False):
    winners = 0
    expected = len(boards) - 1 if expected_winners is None else expected_winners
    not_won = None
    won = None

    for board in boards:
        if board_won(board):
            winners += 1
            won = board
        else:
            not_won = board

    return_board = won if return_winner else not_won
    return return_board if winners == expected else None


def hit_number(number, boards, expected_winners=None, return_winner=False):
    new_boards = []
    for board in boards:
        new_board = []
        for row in board:
            new_row = [element if element != number else None for element in row]
            new_board.append(new_row)
        board = new_board
        new_boards.append(board)

    return new_boards, find_winner(new_boards, expected_winners=expected_winners, return_winner=return_winner)


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
        all_numbers = [int(number) for number in bingo_input.split(",")]
        remainders = None

        for index in range(len(all_numbers)):
            drawn = all_numbers[index]
            boards, winner = hit_number(drawn, boards)
            if winner is not None:
                remainders = all_numbers[(index + 1):]
                break

        boards = remove_winners(boards)
        for index in range(len(remainders)):
            drawn = remainders[index]
            boards, winner = hit_number(drawn, boards, expected_winners=1, return_winner=True)
            if winner is not None:
                break

        winner_sum = 0
        for row in winner:
            for value in row:
                winner_sum += int(value) if value is not None else 0

        print(f"The bingo winner result is {winner_sum * drawn} for {input_file}!")
