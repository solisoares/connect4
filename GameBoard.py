# TODO 
# Create empty Board [OK]
# Show Board         [OK]
# Ask Move
# Valid Move         [OK]
#   \_ Warning       [OK]
#   \_ Update Board  [OK]
# Is Game Over 

class GameBoard():
    def __init__(self, rows: int, columns: int):
        """Construct empty game board of shape rows x columns (MxN)

        Args:
            rows (int): Number of board rows
            columns (int): Number of board columns
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

    def get_row(self, row_idx: int):
        """Get a row from the board 

        Args:
            row_idx (int): idx of the row to get
        
        Returns:
            row (str): The row from the specified index
        """
        row = self.board[row_idx] 
        # row = "".join(row) # FIXME 
        return row

    def get_column(self, column_idx: int):
        """Get a column from the board

        Args:
            column_idx (int): idx of the row to get

        Returns:
            column (list): The column from the specified index
        """
        column = []
        for row in self.board:
            column.append(row[column_idx]) 
        return column

    def get_diagonal(self):
        pass

    def __valid_move(self, column_idx: int):
        """Returns if a game movement is valid or not (If the column is 
        yet to be filled or is already full).

        Args:
            column_idx (int): idx of the column to get

        Returns:
            Bool: Return True or False for the movement validity
        """
        column = self.get_column(column_idx)
        return "_" in column

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
