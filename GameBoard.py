class GameBoard():
    def __init__(self, rows: int = 6, columns: int = 7):
        """Construct empty game board of shape rows x columns (MxN)

        Args:
            rows (int): Number of board rows. Defaults to 6
            columns (int): Number of board columns. Defaults to 7

        Returns:
            None
        """
        self.rows = rows
        self.columns = columns
        self.board = self.create_empty_board()

    def create_empty_board(self):
        """Create empty board game.
        Implemented as a 2D-Matrix (list of lists).

        Args:
            None

        Returns:
            board (list): The empty game board.
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
            for item in row:
                print(item, end="  ")
            print()
        print()

    def get_column(self, column_idx: int):
        """Get a single column from the board

        Used to check move availability and to update the column.

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
        """Get all the diagonals from the board, forward and backward.

        Used in game win check.

        Args:
            None

        Returns:
            List: All the diagonals, list of lists
        """
        max_col = len(self.board[0])
        max_row = len(self.board)
        fdiagonals = [[] for _ in range(max_row + max_col - 1)]
        bdiagonals = [[] for _ in range(len(fdiagonals))]
        for x in range(max_col):
            for y in range(max_row):
                fdiagonals[x+y].append(self.board[y][x])
                bdiagonals[x-y+max_row-1].append(self.board[y][x])
        return fdiagonals + bdiagonals


    def __outside_column_range(self, column_idx: int):
        """ Inform if the choosen column is outside column range.

        Args:
            column_idx (int): idx of the column to get

        Returns:
            Boolean: True or False for outside column range
        """
        return (column_idx < 0) or (column_idx >= self.columns)

    def __valid_move(self, column_idx: int):
        """Returns if a game movement is valid or not.
        
        A valid move is the one that falls inside the game board 
        and the chosen column has free space.

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
        """Returns where to update the column.

        Called only if it is a valid move in `update_board` method.

        Args:
            column_idx (int): idx of the column to get

        Returns:
            char_count (int): the index to update the column
        """
        column = self.get_column(column_idx)
        char_count = 0
        for item in column:
            if item == "_":
                char_count +=1
        return char_count - 1

    def update_board(self, column_idx: int, char: str):
        """Updates board with specified character. 
        
        The board is only updated if it is a valid move.
        Invoked inside `Player.make_move` method.

        Args:
            column_idx (int): idx of the column to get
            char (str): alphanumeric character. Do not use "_"

        Returns:
            None
        """

        if self.__valid_move(column_idx):
            row_idx = self.__row_idx_to_update(column_idx)
            self.board[row_idx][column_idx] = char
        else:
            new_column_idx = int(input("!!! Please, choose a valid column !!!:  "))
            self.update_board(new_column_idx, char)

    def tie(self):
        """ Checks if a tie occured

        Tie is when the board is full and no one won the game.

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


    def win_at_row(self, p1, p2):
        """Checks if any of the players won the game by looking at the rows

        To win at a row, one must put 4 of its character in sequence horizontally

        Args:
            p1 (Player): player 1 from class Player / Player.Machine
            p2 (Player): player 2 from class Player / Player.Machine

        Returns:
            0, 1, 2 (int): Who won the game. No one (0), player 1 (1), player 2 (2)
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
        """Checks if any of the players won the game by looking at the columns

        To win at a column, one must put 4 of its character in sequence vertically

        Args:
            p1 (Player): player 1 from class Player / Player.Machine
            p2 (Player): player 2 from class Player / Player.Machine

        Returns:
            0, 1, 2 (int): Who won the game. No one (0), player 1 (1), player 2 (2)
        """        
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
        """Checks if any of the players won the game by looking at the diagonals

        To win at a diagonal, one must put 4 of its character in sequence diagonally

        Args:
            p1 (Player): player 1 from class Player / Player.Machine
            p2 (Player): player 2 from class Player / Player.Machine

        Returns:
            0, 1, 2 (int): Who won the game. No one (0), player 1 (1), player 2 (2)
        """
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
        """Checks if the game is over

        Args:
            p1 (Player): player 1 from class Player / Player.Machine
            p2 (Player): player 2 from class Player / Player.Machine

        Returns:
            Bool: Whether the game is over or not
        """
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