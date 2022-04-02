#!/usr/bin/python3
from GameBoard import GameBoard
from Player import Player, Machine
from logo import logo

# Print Game Logo
print(logo)

# Create Standard Board
board = GameBoard()
board.show_board()

# Set Game Mode
mode = int( input( "Do you want to play against a human (0) or a machine (1)?  " ) )

# Create Players
if mode == 0:
    p1, p2 = Player("X"), Player("O")
elif mode == 1:
    p1, p2 = Player("X"), Machine("O")

# Game Loop
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
