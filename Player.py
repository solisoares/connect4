from __future__ import annotations
from GameBoard import GameBoard
import random

# TODO 
# make a move [OK]
# make players actually update board and let (maybe)

class Player():
    def __init__(self, char: str):
        """ Construct Player object by specifying the alphanumeric char."""
        self.char = char

    def make_move(self, column_idx: int, board: GameBoard):
        """Make a move on the gamebord.
        Choose a column and your char will be displayed in the
        upper most location available, if the column if filled
        return a message asking a new move.

        Args:
            column_idx (int): column to make the move.
            board (GameBoard): The game board.
        """
        board.update_board(column_idx, self.char)

class Machine(Player):
    def __init__(self, char: str):
        """ Construct Machine object by specifying the alphanumeric char."""
        self.char = char

    def make_move(self, board: GameBoard):
        """Make a random move on the gamebord.
        Choose randonly a column and your char will be displayed in the
        upper most location available, if the column is filled
        return a message asking a new move.

        Args:
            board (GameBoard): The game board.
        """
        column_idx = random.randint(0, len(board.board) - 1)
        board.update_board(column_idx, self.char)
