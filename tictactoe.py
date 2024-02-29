import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board): # This method determines the next player
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O # If "X" count and "O" count are equal on the board, the turn is "X", otherwise it is "O"

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set() # We create an empty set
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j)) # We go through the entire board and add the empty ones to the possible_actions set
    return possible_actions


def result(board, action): # This method returns the new game board resulting from a particular move being played.
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action # coordinates of the move to be played
    player_mark = player(board) # we find the next player
    new_board = [row[:] for row in board] # We create a copy of the current game board.
    new_board[i][j] = player_mark # We apply the specified move to the new board.
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player_mark in [X, O]: # we will check the win status for both players one by one
        # Check rows and columns
        for i in range(3): # If any row or column is filled in entirely by a player, the game win
            if all(board[i][j] == player_mark for j in range(3)) or \
               all(board[j][i] == player_mark for j in range(3)):
                return player_mark
        # Check diagonals
        if all(board[i][i] == player_mark for i in range(3)) or \
           all(board[i][2-i] == player_mark for i in range(3)):
            return player_mark # The game win if any diagonal is completely filled by the player
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    #We look at all points one by one and return true if there is no empty space, false if there is.
    return winner(board) is not None or all(all(cell is not EMPTY for cell in row) for row in board)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


# This function contains the main logic of the Minimax algorithm and aims to choose the best move in the current state of the game.
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # First, it checks whether the game is over or not with the terminal(board) function. If the game is over  it returns None.
    if terminal(board):
        return None

    curr_player = player(board) # Determines the next player.

    # If it is X's turn, it tries to choose the move with the highest utility value of X. It uses the max_value function for this.
    if curr_player == X:
        best_value = -math.inf
        best_move = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action
    # If it is O's turn , it tries to choose the move with O's lowest utility value. It uses the min_value function for this.
    else:
        best_value = math.inf
        best_move = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action

    return best_move # Finally, it returns the best move chosen.


# This function aims to choose the move with the highest utility value in order X.
def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action))) # For each move, it evaluates the other player's (O's) worst case by calling the min_value function.
    return v # It selects the move with the highest utility value and returns this value.


# This function aims to choose the move that has the lowest utility value in the O row.
def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action))) # For each move, it evaluates the other player's (X's) best situation by calling the max_value function.
    return v # It selects the move with the lowest utility value and returns this value.
