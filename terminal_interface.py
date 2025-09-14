import random

class TerminalInterface:
    """
    Provides a terminal-based interface for playing and simulating the Knight Tour.

    This class was made after completing all other parts of the assignment and making the game solely based on a graphical interface. 
    Due to this there is some code reusability.

    Attributes:
        chessboard (Chessboard): The chessboard object representing the state of the board.
        knight_tour (KnightTour): The knight tour object containing logic for valid moves.
    """

    def __init__(self, chessboard, knight_tour):
        """
        Initializes the TerminalInterface with the provided Chessboard and KnightTour objects.

        Args:
            chessboard (Chessboard): The chessboard object to track the state of the board.
            knight_tour (KnightTour): The knight tour logic manager.
        """
        self.chessboard = chessboard
        self.knight_tour = knight_tour
    
    def game(self):
        """
        Starts the game by prompting the user to select a mode (manual or random) and input a starting position.

        If the user enters an invalid mode, the game is restarted.
        """
        tour_type = int(input("Select mode: 1 = manual tour, 2 = random tour:"))
        self.chessboard.print_board()

        if tour_type == 1 or tour_type == 2:
            start_x = int(input("Enter the starting x coordinate:"))
            start_y = int(input("Enter the starting y coordinate:"))

            self.chessboard.move = 1
            self.chessboard.mark_square(start_x, start_y, self.chessboard.move)
            self.chessboard.print_board()

            if tour_type == 1:
                self.manual(start_x, start_y)
            else:
                self.random(start_x, start_y)
        else:
            self.game()
    
    def manual(self, start_x, start_y):
        """
        Executes a manual Knight Tour where the user inputs each move.

        Args:
            start_x (int): The starting x-coordinate.
            start_y (int): The starting y-coordinate.
        """
        current_x = start_x - 1
        current_y = start_y - 1

        while len(self.knight_tour.next_valid_moves(current_x, current_y)) > 0:
            new_x = int(input("Enter x coordinate:")) - 1
            new_y = int(input("Enter y coordinate:")) - 1

            if self.knight_tour.is_valid_move(current_x, current_y, new_x, new_y):
                current_x = new_x
                current_y = new_y
                self.chessboard.move += 1

                self.chessboard.mark_square(current_x + 1, current_y + 1, self.chessboard.move)
                self.chessboard.print_board()
            else:
                print("Invalid move.")
    
    def random(self, start_x, start_y):
        """
        Executes a random Knight Tour where moves are chosen automatically.

        Args:
            start_x (int): The starting x-coordinate.
            start_y (int): The starting y-coordinate.
        """
        current_x = start_x - 1
        current_y = start_y - 1

        while len(self.knight_tour.next_valid_moves(current_x, current_y)) > 0:
            new_move = random.choice(self.knight_tour.next_valid_moves(current_x, current_y))
            current_x = new_move[0] 
            current_y = new_move[1]
            self.chessboard.move += 1
            
            self.chessboard.mark_square(current_x + 1, current_y + 1, self.chessboard.move)
            self.chessboard.print_board()