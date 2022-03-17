from __future__ import annotations
from GameBoard import GameBoard
import random

# TODO 
# [] Fazer que o make_move de `Machine` siga o Princípio de Substituição de Liskove,
#    que diz que uma instância de uma classe deve ser substituível por uma instância 
#    de uma sub-classe sem quebrar o programa. Evitando de usar isinstance em `Game.py`

class Player():
    def __init__(self, char: str):
        """ Construct Player object by specifying the alphanumeric char."""
        self.char = char

    def make_move(self, column_idx: int, board: GameBoard):
        """Make a move on the gamebord.

        Choose a column to make a move in the game board.

        Args:
            column_idx (int): column to make the move.
            board (GameBoard): The game board to make a move..
        """
        board.update_board(column_idx, self.char)

class Machine(Player):
    def __init__(self, char: str):
        """ Construct Machine object by specifying the alphanumeric char."""
        self.char = char

    def make_move(self, board: GameBoard):
        """Make a random move on the gamebord.
        
        A column is randomly selected inside the possible range, but this column
        may be already filled. If that is the case, try again until the movement 
        validity is achieved.

        Args:
            board (GameBoard): The game board to make a move.
        """
        column_idx = random.randint(0, len(board.board[0]) - 1) # Try a initial random number in the range of the number of columns
        while board._GameBoard__valid_move(column_idx) == False: 
            column_idx = random.randint(0, len(board.board[0]) - 1) # If invalid move, try again
        board.update_board(column_idx, self.char) # When valid move is achieved, update board
