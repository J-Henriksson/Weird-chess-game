class Chessboard:
    """
    A chessboard for the knight to move across.

    Attributes:
        size (int): The size of the chessboard.
        board (list[list[int]]): A 2D list representing each square/position on of the board.
        move (int): The current move number.
    """

    def __init__(self, size):
        """
        Initializes the chessboard with the provided size and sets all squares to unvisited.

        Args:
            size (int): The size of the chessboard.
        """
        self.size = size
        self.board = []
        self.move = 0

        for row in range(size):
            self.board.append([])
            for column in range(size):
                self.board[row].append(0)
    
    def mark_square(self, x, y, move):
        """
        Marks a square on the board as visited with the current move number.

        Args:
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            move (int): The current move.
        """

        self.board[y - 1][x - 1] = move

    def reset_board(self):
        """
        Resets the board and move count to their initial states.
        """

        for row in self.board:
            for column in range(len(row)):
                row[column] = 0
        self.move = 0

    def print_board(self):
        """
        Prints the current state of the chessboard in the terminal.
        """

        print("-----------")
        for column in range(len(self.board)):
            print(self.board[len(self.board) - 1 - column])