"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def minimax_value(board,player,a,b):
    if terminal(board):
        return utility(board)
    if player == X:
        v = -1
        for action in actions(board):
            v=max(v,minimax_value(result(board, action),O,a,b))
            a=max(a,v)
            if a>=b:
                break
        return v
    else:
        v = 1
        for action in actions(board):
            v=min(v,minimax_value(result(board, action),X,a,b))
            b=min(b, v)
            if a>=b:
                break
        return v

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count=0
    for i in range(3):
        for j in range(3):
            if board[i][j]!=EMPTY:
                count+=1
    
    if board==initial_state():
        return X
    if count%2==1:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                moves.add((i,j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Gaand marale")
    brd=copy.deepcopy(board)
    brd[action[0]][action[1]] = player(board)
    return brd


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
            else:
                return None
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == X:
                return X
            elif board[0][j] == O:
                return O
            else:
                return None
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
        else:
            return None
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] == X:
            return X
        elif board[2][0] == O:
            return O
        else:
            return None
    return None
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] != None:
                return True
            else:
                return False
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] != None:
                return True
            else:
                return False
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != None:
            return True
        else:
            return False
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] != None:
            return True
        else:
            return False
    for i in range(3):
        for j in range(3):
            if  board[i][j] == None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == X:
                return 1
            elif board[i][0] == O:
                return -1
            else:
                return 0
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == X:
                return 1
            elif board[0][j] == O:
                return -1
            else:
                return 0
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return 1
        elif board[0][0] == O:
            return -1
        else:
            return 0
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] == X:
            return 1
        elif board[2][0] == O:
            return -1
        else:
            return 0
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    optimal=None
    a=-1
    b=1
    if player(board) is X:
        v=-1
        for action in actions(board):
            new_v=minimax_value(result(board, action),O,a,b)
            a=max(v, new_v)
            if new_v > v:
                v=new_v
                optimal=action
    else:
        v = 1
        for action in actions(board):
            new_v = minimax_value(result(board, action),X,a,b)
            b=min(v,new_v)
            if new_v < v:
                v=new_v
                optimal=action
    return optimal 