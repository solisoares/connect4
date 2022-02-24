from GameBoard import GameBoard
from Player import Player, Machine
from logo import logo

# Game Logo
print(logo)

# Board
# rows = int(input("Please, how many rows do you want the board to be?  "))
# columns = int(input("Please, how many columns do you want the board to be?  "))
board = GameBoard()
board.show_board()

# Players
mode = int( input( "Do you want to play against a human (0) or a machine (1)?  " ) )
if mode == 0:
    p1, p2 = Player("x"), Player("o")
elif mode == 1:
    p1, p2 = Player("x"), Machine("o")

# Game
while True:
    game_over = board.game_over
    column = int(input("Please select a column Player 1:"))
    p1.make_move(column, board)
    print("\n"*100)
    if game_over(p1, p2):
        board.show_board()
        break
    board.show_board()

    if isinstance(p2, Machine):
        p2.make_move(board)
        print("\n"*100)
        if game_over(p1, p2):
            board.show_board()
            break
        board.show_board()
    else:
        column = int(input("Please select a column Player 2:"))
        p2.make_move(column, board)
        print("\n"*100)
        if game_over(p1, p2):
            board.show_board()
            break
        board.show_board()