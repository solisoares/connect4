from GameBoard import GameBoard
from Player import Player

# Board
board = GameBoard(rows=3, columns=4)

# Players
sula  = Player(char="x")
xande = Player(char="o")

# Game
sula.make_move(0, board)
sula.make_move(0, board)
sula.make_move(0, board)
xande.make_move(0, board)

# Show Board
board.show_board()