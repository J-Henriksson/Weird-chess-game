import pygame
import sys

class UserInteraction:
    """
    Handles user interaction and visualization for the knight tour.

    Attributes:
        chessboard (Chessboard): The chessboard object to represent graphically.
        square_size (int): The size of each square on the chessboard.
        board_size (int): The total size of the chessboard in pixels.
        screen: The Pygame window for displaying the board.
        knight_sprite: The icon representing the knight piece.
        font: The font used for rendering text on the board.
    """

    def __init__(self, chessboard):
        """
        Initializes the UserInteraction class with the given chessboard and sets up Pygame for visualization.

        Args:
            chessboard (Chessboard): The chessboard object containing the board state.
        """

        pygame.init()
        self.chessboard = chessboard
        self.square_size = 80
        self.board_size = chessboard.size * self.square_size
        self.screen = pygame.display.set_mode((self.board_size, self.board_size))
        pygame.display.set_caption('Knight Tour')
        self.knight_sprite = pygame.image.load('assets/knight.png')
        self.knight_sprite = pygame.transform.scale(self.knight_sprite, (self.square_size, self.square_size))
        self.font = pygame.font.Font(None, 36)

    def draw_board(self):
        """
        Draws the chessboard on the screen.
        """

        colors = [(255, 255, 255), (0, 0, 0)]
        for row in range(self.chessboard.size):
            for col in range(self.chessboard.size):
                color = colors[(row + col) % 2]
                pygame.draw.rect(self.screen, color, pygame.Rect(col * self.square_size, row * self.square_size, self.square_size, self.square_size))

    def draw_knight(self):
        """
        Draws the knight piece and move numbers on the board.
        """

        for row in range(self.chessboard.size):
            for col in range(self.chessboard.size):
                if self.chessboard.board[row][col] != 0 and self.chessboard.board[row][col] == self.chessboard.move:
                    self.screen.blit(self.knight_sprite, (col * self.square_size, (self.chessboard.size - 1 - row) * self.square_size))
                elif self.chessboard.board[row][col] != 0:
                    text = self.font.render(str(self.chessboard.board[row][col]), True, (255, 0, 0))
                    text_rect = text.get_rect(center=(col * self.square_size + self.square_size // 2, (self.chessboard.size - 1 - row) * self.square_size + self.square_size // 2))
                    self.screen.blit(text, text_rect)
    
    def mark_squares_green(self, coordinates):
        """
        Highlights all valid squares that the knight can move to in green.

        Args:
            coordinates (list[list[int]]): A list of coordinates for valid moves.
        """

        color = (0, 255, 0)
        for squares in coordinates:
            pygame.draw.rect(self.screen, color, pygame.Rect(squares[0] * self.square_size, (self.chessboard.size - 1 - squares[1]) * self.square_size, self.square_size, self.square_size))
        
        pygame.display.flip()

    def update_display(self):
        """
        Updates the display by drawing the board and the knight.
        """

        self.draw_board()
        self.draw_knight()
        pygame.display.flip()

    def display_board(self):
        """
        Continuously displays the board until the user quits.
        """

        running = True
        clock = pygame.time.Clock()
        while running:
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.update_display()
            clock.tick(30)
        pygame.quit()
    
    def click_to_coordinates(self):
        """
        Waits for the user to click on the screen and returns the chessboard coordinates of the click.

        Returns:
            list[int, int]: The x and y-coordinates of the clicked square.
        """

        waiting_for_click = True
        coordinates = []
        while waiting_for_click:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    col = x // self.square_size
                    row = (self.board_size - y) // self.square_size 
                    coordinates = [col, row]
                    waiting_for_click = False
                    break
        return coordinates