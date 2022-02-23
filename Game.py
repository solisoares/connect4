from GameBoard import GameBoard
from Player import Player, Machine

# Board
# rows = int(input("Please, how many rows do you want the board to be?  "))
# columns = int(input("Please, how many columns do you want the board to be?  "))
rows, columns = 6,7
board = GameBoard(rows, columns)
board.show_board()

# Players
mode = int( input( "Do you want to play against a human (0) or a machine (1)?  " ) )
if mode == 0:
    p1, p2 = Player("x"), Player("o")
elif mode == 1:
    p1, p2 = Player("x"), Machine("o")

# Game
while True:
    column = int(input("Please select a column Player 1:"))
    p1.make_move(column, board)
    board.show_board()

    if isinstance(p2, Machine):
        p2.make_move(board)
        board.show_board()
    else:
        column = int(input("Please select a column Player 2:"))
        p2.make_move(column, board)
        board.show_board()
