from constants import BLANK


def trios(board):
    return (
        board[0:3],
        board[3:6],
        board[6:9],
        board[0:7:3],
        board[1:8:3],
        board[2:9:3],
        board[0:9:4],
        board[2:8:2],
    )


def win(player, board):
    match = player * 3
    for trio in trios(board):
        if trio == match:
            return True


def winnable(player, board):
    for trio in trios(board):
        if trio in {player+player+BLANK, player+BLANK+player, BLANK+player+player}:
            return True
    return False


def num_winnable(player, board):
    return sum(1 for trio in trios(board) if trio in {player+player+BLANK, player+BLANK+player, BLANK+player+player})


def print_board(board):
    print board[0:3].replace('', ' ')[1:-1]
    print board[3:6].replace('', ' ')[1:-1]
    print board[6:9].replace('', ' ')[1:-1]