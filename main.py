from chessboard import Chessboard
from knight_tour import KnightTour
from user_interaction import UserInteraction
from menu import Menu

#Main entry point for the program.
if __name__ == "__main__":
    chessboard = Chessboard(8)
    ui = UserInteraction(chessboard)
    
    knight_tour = KnightTour(chessboard, ui)
    menu = Menu(640, 640, chessboard, knight_tour, ui)

    menu.main_menu()
