class GameBoard():
    def __init__(self, rows: int = 6, columns: int = 7):
        """Construct empty game board of shape rows x columns (MxN)

        Args:
            rows (int): Number of board rows. Defaults to 6
            columns (int): Number of board columns. Defaults to 7
        """
        self.rows = rows
        self.columns = columns
        self.board = self.create_empty_board()

    def create_empty_board(self):
        """Create empty board game.
        Implemented as a 2D-Matrix (list of list).

        Args:
            None

        Returns:
            board (list): The game board.
        """
        board = []
        for row in range(self.rows):
            board.append(["_"] * self.columns)
        return board

    def show_board(self):
        """ Show the game board in a nice way

        Args:
            None

        Returns:
            None
        """
        print()
        [print(n, end="  ") for n in range(self.columns)]
        print()
        for row in self.board:
            # print(" " * 10, end="")
            for item in row:
                print(item, end="  ")
            print()
        print()

    # def get_row(self, row_idx: int):
    #     """Get a row from the board 

    #     Args:
    #         row_idx (int): idx of the row to get
        
    #     Returns:
    #         row (str): The row from the specified index
    #     """
    #     row = self.board[row_idx] 
    #     return row

    def get_column(self, column_idx: int):
        """Get a column from the board

        Args:
            column_idx (int): idx of the column to get

        Returns:
            column (list): The column from the specified index
        """
        column = []
        for row in self.board:
            column.append(row[column_idx]) 
        return column

    def get_diagonals(self):
        max_col = len(self.board[0])
        max_row = len(self.board)
        all_diagonals = [[] for _ in range(max_row + max_col - 1)]
        for x in range(max_col):
            for y in range(max_row):
                all_diagonals[x+y].append(self.board[y][x])
        return all_diagonals

    def __outside_column_range(self, column_idx: int):
        """ Inform whether column_idx is outside column range or inside

        Args:
            column_idx (int): idx of the column to get

        Returns:
            Boolean: True or False for outside or inside column range
        """
        return (column_idx < 0) or (column_idx >= self.columns)

    def __valid_move(self, column_idx: int):
        """Returns if a game movement is valid or not (If the column is 
        yet to be filled or is already full).

        Args:
            column_idx (int): idx of the column to get

        Returns:
            Bool: Return True or False for the movement validity
        """
        if self.__outside_column_range(column_idx): # Checks if idx is not in column range
            return False
        else:
            column = self.get_column(column_idx)
        return ("_" in column)  # If idx in column range, checks if there is "_" in the column

    def __row_idx_to_update(self, column_idx: int):
        """Returns the idx to update in column if is valid move in
        that column

        Args:
            column_idx (int): idx of the column to get

        Returns:
            char_count (int) or string: returns the index to update or message
                warning that it must be a valid column
        """
        column = self.get_column(column_idx)
        char_count = 0
        for item in column:
            if item == "_":
                char_count +=1
        return char_count - 1

    def update_board(self, column_idx: int, char: str):
        """Updates board with specified character. 
        Invoked by Player.make_move method.

        Args:
            column_idx (int): idx of the column to get
            char (str): alphanumeric character. Do not use "_"
        """

        if self.__valid_move(column_idx):
            row_idx = self.__row_idx_to_update(column_idx)
            self.board[row_idx][column_idx] = char
        else:
            # print("Please, choose a valid column")
            new_column_idx = int(input("!!! Please, choose a valid column !!!:  "))
            self.update_board(new_column_idx, char)

    def tie(self):
        """Checks if the board is full and no one won the game

        Args:
            None

        Returns:
            Boolean: True/False to whether it is a tie or not
        """
        # Checks if there is "_" present in the board elements
        for row in self.board:
            for item in row:
                if "_" in item:
                    return False # "_" char found, not a tie
        return True # "_" char found, its a tie

    # def winner_char_count(self, list, p1, p2):
    #     p1_count, p2_count = 0, 0
    #     for item in list:
    #         if p1.char == item:
    #             p1_count += 1
    #             p2_count = 0
    #             if p1_count == 4:
    #                 return 1
    #         elif p2.char == item:
    #             p2_count += 1
    #             p1_count = 0
    #             if p2_count == 4:
    #                 return 2
    #     return 0
    
    def win_at_row(self, p1, p2): # TODO: ask professor about import class Player here the problem is that i import GameBoard class in Player already
        """Checks if any of the players won the game by looking at the rows

        Args:
            p1 (Player): player 1 from class Player/Player.Machine
            p2 (Player): player 2 from class Player/Player.Machine

        Returns:
            0, 1, 2 (int): Who won the game. No one (0), player 1 (1); player 2 (2)
        """
        for row in self.board:
            p1_count, p2_count = 0, 0
            for row_item in row: # for each row look at each item
                if p1.char == row_item:
                    p1_count += 1
                    p2_count = 0
                    if p1_count == 4:
                        return 1
                elif p2.char == row_item:
                    p2_count += 1
                    p1_count = 0
                    if p2_count == 4:
                        return 2
                elif "_" == row_item:
                    p1_count = 0
                    p2_count = 0
        return 0 # Neither players won

    def win_at_column(self, p1, p2):
        for column_idx in range(len(self.board[0])):
            p1_count, p2_count = 0, 0
            for row_idx in range(len(self.board)):
                column_item = self.board[row_idx][column_idx]
                if p1.char == column_item:
                    p1_count += 1
                    p2_count = 0
                    if p1_count == 4:
                        return 1
                elif p2.char == column_item:
                    p2_count += 1
                    p1_count = 0
                    if p2_count == 4:
                        return 2
        return 0 # Neither players won

    def win_at_diagonal(self, p1, p2):
        diagonals = self.get_diagonals()
        for row in diagonals:
            p1_count, p2_count = 0, 0
            for row_item in row: # for each row look at each item
                if p1.char == row_item:
                    p1_count += 1
                    p2_count = 0
                    if p1_count == 4:
                        return 1
                elif p2.char == row_item:
                    p2_count += 1
                    p1_count = 0
                    if p2_count == 4:
                        return 2
        return 0 # Neither players won        

    def game_over(self, p1, p2):
        # Check game over by row
        winner = self.win_at_row(p1, p2)
        if winner != 0:
            print(f"Player {winner} is the winner!!")
            print(f"------------------------")
            return True
        
        # Check game over by column
        winner = self.win_at_column(p1, p2)
        if (winner == 1) or (winner == 2):
            print(f"Player {winner} is the winner!!")
            print(f"------------------------")
            return True

        # Check game over by diagonal
        winner = self.win_at_diagonal(p1, p2)
        if (winner == 1) or (winner == 2):
            print(f"Player {winner} is the winner!!")
            print(f"------------------------")
            return True

        # Check tie
        if self.tie():
            print(f"It's a Tie!!")
            print(f"------------")    
            return True