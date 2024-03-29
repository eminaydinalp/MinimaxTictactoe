# Tictactoe Game Using Minimax Algorithm With Python

The basic idea behind minimax is that we want to know how to play when we assume our opponent will play the best moves possible.

The minimax algorithm applies this strategy recursively from any given position - we explore the game from a given starting position until we reach all possible end-of-game states. We can represent this as a tree, with each level of the tree showing the possible board positions for a given player’s turn. When we reach an end-of-game state, there’s no choice to be made, so the value is the game result, that is 1 if X won, -1 if O won, and 0 if it was a draw. If it is X’s turn and it’s not a final board state, we choose the maximum of the values of the next possible moves from that position in the tree. This represents the best possible option for X. If it is O’s turn, then we choose the minimum of these values, which is the best option for O. We keep propagating the position values upward toward the root position, alternating between maximum and minimum values as we go - which is of course where the minimax algorithm gets its name.

The diagram below shows an example of minimax applied to a board position:


<img width="819" alt="Screenshot 2024-02-29 at 16 01 34" src="https://github.com/eminaydinalp/MinimaxTictactoe/assets/59748099/cd6ab347-7b94-4b08-a6b6-707ac3346b6e">

## Using Methods : 

<img width="804" alt="Screenshot 2024-02-29 at 16 26 02" src="https://github.com/eminaydinalp/MinimaxTictactoe/assets/59748099/a9382390-fdb9-408e-af5c-2c812daeeaa5">

# MINIMAX Algorithm

When it comes to artificial intelligence, the minimax algorithm works : 

If it is X's turn, it tries to choose the move with the highest utility value of X. This is O's minimum value.



<img width="599" alt="Screenshot 2024-02-29 at 16 31 17" src="https://github.com/eminaydinalp/MinimaxTictactoe/assets/59748099/347ff373-d332-47cb-98eb-ff05a60b55da">



min_value : This function aims to choose the move that has the lowest utility value in the O row.



<img width="454" alt="Screenshot 2024-02-29 at 16 42 48" src="https://github.com/eminaydinalp/MinimaxTictactoe/assets/59748099/716db04e-149e-4e77-bc21-dcbdeddfe9d0">



If it is O's turn , it tries to choose the move with O's lowest utility value. This is X's maximum value.



<img width="578" alt="Screenshot 2024-02-29 at 16 45 19" src="https://github.com/eminaydinalp/MinimaxTictactoe/assets/59748099/c98015e1-04c1-4052-a2c6-c26ca28814dd">



max_value : This function aims to choose the move with the highest utility value in order X.



<img width="476" alt="Screenshot 2024-02-29 at 16 45 45" src="https://github.com/eminaydinalp/MinimaxTictactoe/assets/59748099/fdfde449-9cb7-4ed9-820d-0d9ce6a2b9ed">



