import pygame

class Menu:
    """
        Handles the menu that allows users to navigate between the different tours and the simulation.

        Attributes:
            screen: The Pygame screen where the menus and game visuals are displayed.
            font: Font used for the start button.
            small_font: Font used for the mode selection buttons.
            chessboard: The chessboard object used to reset the board once the user exits back to the mode selection after a tour.
            ui: The user interaction object for managing graphics.
            knight_tour: The knight tour object that manages the movement logic. This connects to the buttons.
        """
    
    def __init__(self, screen_width, screen_height, chessboard, knight_tour, user_interaction):
        """
        Initializes the Menu class.

        Args:
            screen_width (int): Width of the screen/window.
            screen_height (int): Height of the screen/window.
            chessboard: The chessboard object used to reset the board once the user exits back to the mode selection after a tour.
            knight_tour: The knight tour object that manages the movement logic (and contains a chessboard object).
            user_interaction: The user interaction object for managing graphics.
        """

        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Knight Tour Menu')
        self.font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 36)

        self.chessboard = chessboard
        self.ui = user_interaction
        self.knight_tour = knight_tour

    def draw_start_button(self):
        """
        Draws the start button on the screen.

        Returns:
            pygame.Rect: The rectangle representing the start button.
        """

        start_button = pygame.Rect(self.screen.get_width() // 2 - 100, self.screen.get_height() // 2 - 25, 200, 50)
        pygame.draw.rect(self.screen, (0, 128, 0), start_button)
        text = self.font.render('Start', True, (255, 255, 255))
        text_rect = text.get_rect(center=start_button.center)
        self.screen.blit(text, text_rect)
        return start_button

    def draw_main_menu_buttons(self):
        """
        Draws the main menu buttons (Manual, Random, Simulation) on the screen.

        Returns:
            list[pygame.Rect]: A list of rectangles representing the buttons.
        """

        buttons = []
        button_labels = ['Manual', 'Random', 'Simulation']
        positions = [(self.screen.get_width() // 2 - 160, self.screen.get_height() // 2 - 25),
                     (self.screen.get_width() // 2 + 20, self.screen.get_height() // 2 - 25),
                     (self.screen.get_width() // 2 - 70, self.screen.get_height() // 2 + 75)]

        for i, label in enumerate(button_labels):
            button = pygame.Rect(positions[i][0], positions[i][1], 140, 50)
            pygame.draw.rect(self.screen, (0, 128, 0), button)
            text = self.small_font.render(label, True, (255, 255, 255))
            text_rect = text.get_rect(center=button.center)
            self.screen.blit(text, text_rect)
            buttons.append(button)
        return buttons

    def main_menu(self):
        """
        Displays the main menu with a start button.
        """

        running = True
        while running:
            self.screen.fill((0, 0, 0))
            start_button = self.draw_start_button()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(event.pos):
                        running = False
                        self.select_mode_menu()

        pygame.quit()
    
    def select_mode_menu(self):
        """
        Displays the mode selection menu with options for Manual, Random, or Simulation.
        """

        running = True
        while running:
            self.screen.fill((0, 0, 0))
            buttons = self.draw_main_menu_buttons()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i, button in enumerate(buttons):
                        if button.collidepoint(event.pos):
                            if i == 0:
                                self.knight_tour.random_tour(True, False)
                                self.knight_tour_done()
                            elif i == 1:
                                self.knight_tour.random_tour(False, False)
                                self.knight_tour_done()
                            elif i == 2:
                                self.knight_tour.simulation(1000)
                                self.select_mode_menu()
                            running = False
    
    def knight_tour_done(self):
        """
        Waits for the user to click anywhere on the screen after a tour is done, used to prevent the window from closing directly after the tour is complete.
        Returns to the selection menu if the user clicks on the screen.
        """

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.chessboard.reset_board()
                    self.select_mode_menu()
                    running = False

        pygame.quit()