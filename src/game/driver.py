from gamespace import GameState, Move
from board import print_board, win
from search import minimax
from constants import *

if __name__ == '__main__':
    first = MAX
    game = GameState(first)

    while not game.terminal():
        if game.nextplayer == MIN:
            while 1:
                print 'location: '
                location = raw_input()
                action = Move(MIN, int(location)-1)
                if action.legal(game):
                    break
                else:
                    print 'illegal move'
            game = game.result(action)
            print_board(game.board)
            print
        else:
            move = minimax.MiniMaxSearch().decide_min(game)
            game = game.result(move)
            print_board(game.board)

    if win(MAX, game.board):
        print 'WINNER: '+MAX
    elif win(MIN, game.board):
        print 'WINNER: '+MIN
    else:
        print 'DRAW!'
