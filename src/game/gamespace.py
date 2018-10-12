import board
from search.abstract_statespace import AbstractState, AbstractAction
from constants import MIN, MAX, BLANK


class GameState(AbstractState):
    def __init__(self, nextplayer, board=None):
        self.nextplayer = nextplayer
        self.board = board or BLANK * 9

    def __hash__(self):
        return hash(self.board)

    def result(self, move):
        return GameState(
            nextplayer=MIN if self.max() else MAX,
            board=move.result(self.board)
        )

    def actions(self):
        return [Move(self.nextplayer, i) for i, c in enumerate(self.board) if c is BLANK]

    def max(self):
        return self.nextplayer is MAX

    def terminal(self):
        return self.evaluate() != 0 or self.board.count(BLANK) == 0

    def evaluate(self):
        if board.win(MAX, self.board):
            return 1
        if board.win(MIN, self.board):
            return -1
        return 0

    def trios(self):
        return board.trios(self.board)

    def winnable(self):
        return board.winnable(self.nextplayer, self.board)

    def num_winnable(self):
        return board.num_winnable(self.nextplayer, self.board)


class Move(AbstractAction):
    def __init__(self, piece, loc):
        self.piece = piece
        self.location = loc

    def __repr__(self):
        return "{0}:{1}".format(self.piece, self.location)

    def legal(self, game_state):
        return game_state.board[self.location] is BLANK

    def result(self, board):
        return board[:self.location] + self.piece + board[self.location+1:]