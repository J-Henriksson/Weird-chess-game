import random
import pygame
import matplotlib.pyplot as plt

class KnightTour:
    """
    Manages the knight's movements and the logic of the tour.

    Attributes:
        chessboard (Chessboard): The chessboard object containing the state of the board.
        ui (UserInteraction): The user interaction object used for managing graphics.
        move_sound (pygame.mixer.Sound): Sound effect played after a legal move is made.
        illegal_move_sound (pygame.mixer.Sound): Sound effect played after an illegal move is attempted.
        end_sound (pygame.mixer.Sound): Sound effect played when the last move a tour is made.
    """

    def __init__(self, chessboard, user_interaction):
        """
        Initializes the KnightTour with references to chessboard and user interaction objects, as well as pygame's mixer module.

        Args:
            chessboard (Chessboard): The chessboard object containing the board state.
            user_interaction (UserInteraction): The user interaction object for graphical representation.
        """

        self.chessboard = chessboard
        self.ui = user_interaction
        
        pygame.mixer.init()
        self.move_sound = pygame.mixer.Sound("assets/knight_move_sound1.wav")
        self.illegal_move_sound = pygame.mixer.Sound("assets/illegal_move.wav")
        self.end_sound = pygame.mixer.Sound("assets/game_end.wav")

    def is_valid_move(self, current_x, current_y, x , y):
        """
        Checks if the given move is valid.

        Args:
            current_x (int): The current x-coordinate of the knight.
            current_y (int): The current y-coordinate of the knight.
            x (int): The new x-coordinate to move to.
            y (int): The new y-coordinate to move to.

        Returns:
            bool: True if the move is valid, otherwise False.
        """
        return [x, y] in self.next_valid_moves(current_x, current_y)
        
    def next_valid_moves(self, x, y):
        """
        Generates all valid moves that the knight can make from a given position.

        Args:
            x (int): The current x-coordinate index of the knight.
            y (int): The current y-coordinate index of the knight.

        Returns:
            list[list[int, int]]: A list of valid (x, y) positions that the knight can move to.
        """

        valid_moves = []

        positions = [2, 2, -2, -2, 1, -1, 1, -1]
        for position in range(len(positions)):
            if y + positions[position] < self.chessboard.size and y + positions[position] > -1 and x + positions[len(positions) - 1 - position] < self.chessboard.size and x + positions[len(positions) - 1 - position] > -1:
                if self.chessboard.board[y + positions[position]][x + positions[len(positions) - 1 - position]] == 0:
                    valid_moves.append([x + positions[len(positions) - 1 - position], y + positions[position]])
        
        return valid_moves

    def random_tour(self, manual, simulation):
        """
        Executes a either a random or manual knight tour starting from a given position selected by an on screen click.

        Args:
            manual (bool): If True, allows the user to manually control the knight's movements. If False runs a random tour.
            simulation (bool): If True, runs the tour as a part of the simulation function without user input.
        """

        if not simulation:
            self.ui.update_display()
            click_square = self.ui.click_to_coordinates()
            start_x = click_square[0]
            start_y = click_square[1]

            valid_move = True
        else:
            start_x = random.randint(0, self.chessboard.size - 1)
            start_y = random.randint(0, self.chessboard.size - 1)
        
        self.chessboard.move = 1
        self.chessboard.mark_square(start_x + 1, start_y + 1, self.chessboard.move)
        if not simulation:
            self.ui.update_display()
            self.move_sound.play()
        
        new_moves = self.next_valid_moves(start_x, start_y)
        current_x = start_x 
        current_y = start_y 

        while len(new_moves) > 0:
            self.chessboard.move += 1

            if manual == False or simulation == True:
                new_move = random.choice(new_moves)
                if not simulation:
                    pygame.time.delay(1000)
            else:
                self.ui.mark_squares_green(new_moves)
                click_square = self.ui.click_to_coordinates()

                x_cord = click_square[0]
                y_cord = click_square[1]
                if self.is_valid_move(current_x, current_y, x_cord, y_cord):
                    new_move = [x_cord, y_cord]
                    current_x = x_cord
                    current_y = y_cord
                    valid_move = True
                else:
                    new_move = [current_x, current_y]
                    self.chessboard.move -= 1
                    valid_move = False

            self.chessboard.mark_square(new_move[0] + 1, new_move[1] + 1, self.chessboard.move)
            if not simulation:
                if valid_move:
                    self.ui.update_display()
                    if len(self.next_valid_moves(new_move[0], new_move[1])) == 0:
                        self.end_sound.play()
                    else:
                        self.move_sound.play()
                else:
                    self.illegal_move_sound.play()    

            new_moves = self.next_valid_moves(new_move[0], new_move[1])

    def simulation(self, iterations):
        """
        Runs a simulation of multiple random knight tours, collects statistics on the number of squares visited each run and then displays the results in a histogram.

        Args:
            iterations (int): The number of simulations to run.
        """

        moves_per_run = []

        for simulation in range(iterations):
            self.random_tour(False, True)
            moves_per_run.append(self.chessboard.move)
            self.chessboard.reset_board()

        plt.hist(moves_per_run, bins=20, color='blue', edgecolor='black', alpha=0.7)
        plt.xlabel('Number of Moves')
        plt.ylabel('Frequency')
        plt.title('Distribution of Moves in Knight Tour Simulations')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()