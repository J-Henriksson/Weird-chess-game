# Specifikation

## Inledning

Det här projektet är en simulering av springarens rörelser på ett schackbräde enligt reglerna av spelet. Springaren kan flytta sig två steg vertikalt och sedan ett steg horisontalt, eller två steg horisontalt och sedan ett steg vertikalt. 
Programmet kan köras i terminalen eller via ett grafiskt användargränssnitt. Programmet går ut på att användaren matar in startkoordinaten för springaren och kan sedan antingen välja att själv kontrollera springaren, eller låta programmet göra det. Ifall programmet gör det kommer programmet att slumpmässigt förflytta springaren tills springaren inte längre kan flytta sig utan att gå på en koordinat som tidigare besökts. Användaren kommer också kunna välja att simulera 1000 springarvandringar och samla ihop statistik över hur många rutor springaren passerade i varje simulering. Under programmets gång så kommer en grafisk representation av brädet och springaren att vissa pjäsens förflyttning.


De huvudsakliga utmaningarna är:

- Att implementera en algoritm som validerar vilka drag som är giltiga.
Det här blir svårt eftersom man måste göra en funktionen som hanterar alla möjliga fall och kombinationer som kan ge ogiltiga drag.
Programmet måste kunna hantera drag som är out of bounds, på en ruta som redan besökts eller på ett sätt som inte följer springarens rörelsemönster.

- Att visualisera brädet och springarens rörelser.
Detta är mest tidskrävande eftersom det kräver att jag lär mig mer om pygame som är det biblioteket jag tänkt använda mig av. Jag tror dock att det kommer att bli extra svårt att anpassa grafiken för att användaren ska kunna kontrollera springaren själv.

---

## Användarscenarier

### Upptäcka schack och springarens rörelser
Erik är 14 år och har nyligen börjat spela schack. För att lära sig mer om hur springaren fungerar laddar han ner programmet. Han anger startpositionen C3 och låter programmet själv röra springaren. 
Erik använder det för att se hur springaren rör sig steg för steg över brädet och försöker själv förutsäga vilka drag som är möjliga. När programmet avslutas analyserar han resultatet och börjar förstå hur springaren kan röra sig och hur schack fungerar. Programmet hjälper honom med logik och intuition för spelet.

### En schacklärare som använder programmet för undervisning
Maria är schacklärare och letar efter ett nytt sätt att undervisa sina elever om springarens rörelser. Hon använder programmets grafiska gränssnitt för att demonstrera dragen för sina elever. 
Maria startar programmet och väljer startpositionen E4, hon väljer sedan att själv röra pjäsen istället för att låta låta programmet göra det. I det grafiska fönstret visar hon hur springaren rör sig steg för steg och diskuterar strategier för att nyttja pjäsens rörelsemönster så mycket som möjligt. 
Programmet används som ett pedagogiskt verktyg för att engagera eleverna och hjälpa dom förstå springarens styrkor och begränsningar

### En expert som utmanar sin egen förmåga
Johan är en erfaren schackspelare som vill förbättra sin problemlösningsförmåga. Han använder programmet för att utmana sig själv genom att använda dess funktion som låter spelaren manuellt styra springaren. 
Johan väljer startpositionen A1 och försöker hitta den snabbaste vägen för springaren att besöka alla 64 rutor. Programmet blir ett verktyg för att finslipa hans färdigheter.

---

## Programskelett

```python
class Chessboard:
    """
    Represents a chessboard for the knight to move across. Handles board state, 
    boundaries, and the visualization of the knight's movements.

    Fields:
        size (int): The size of the chessboard.
        board (list[list[int]]): A 2D list representing the board state.
            - `0`: Unvisited square.
            - `k`: Square visited at step `k`.
            - `-1`: Out-of-bounds filler square.
    """
    def __init__(self, size=8):
        """
        Initializes the chessboard with boundaries and sets all squares to unvisited by default.
        
        Args:
            size (int): The size of the chessboard.
        """
        pass

    def mark_square(self, x, y, step):
        """
        Marks a square as visited with the step number.
        
        Args:
            x (int): The row index of the square.
            y (int): The column index of the square.
            step (int): The step number to mark the square with.
        """
        pass

    def reset_board(self):
        """
        Resets the board to its initial unvisited state.
        """
        pass


class KnightTour:
    """
    Manages the knight's movements and the logic of the tour simulation.
    """
    def __init__(self, chessboard):
        """
        Initializes the KnightTour with a reference to a chessboard.
        
        Args:
            chessboard (Chessboard): The chessboard object to interact with.
        """
        pass

    def is_valid_move(self, x, y):
        """
        Checks if a move is valid (within the bounds of the knight and not already visited).
        
        Args:
            x (int): The row index of the square.
            y (int): The column index of the square.
        
        Returns:
            bool: True if the move is valid, False otherwise.
        """
        pass

    def next_valid_moves(self, x, y):
        """
        Generates all valid moves for the knight from a given position.
        
        Args:
            x (int): The current row index of the knight's position.
            y (int): The current column index of the knight's position.
        
        Returns:
            list[tuple[int, int]]: A list of (x, y) positions on the board.
        """
        pass

    def random_tour(self, start_x, start_y):
        """
        Executes a random knight's tour starting from a given position.
        
        Args:
            start_x (int): The starting row index.
            start_y (int): The starting column index.
        """
        pass



class UserInteraction:
    """
    Handles user input, graphical representation, and other user-facing stuff.
    """
    def get_starting_position(self):
        """
        Prompts the user to input the starting position of the knight.
        
        Returns:
            tuple[int, int]: The starting position as (row, column).
        """
        pass

    def graphical_representation(self, chessboard):
        """
        Displays the knight's movements graphically in a separate window.
        
        Args:
            chessboard (Chessboard): The chessboard object containing the simulation state.
        """
        pass

    def simulate_multiple_tours(self, chessboard, iterations=1000):
        """
        Simulates multiple knight's tours and collects statistics on the number of squares visited.
        
        Args:
            chessboard (Chessboard): The chessboard object for resetting and simulating.
            iterations (int): The number of simulations to run.
        """
        pass
```

## Minnet

Funktionaliteten av det här programmet är uppdelat i tre classer: Chessboard, KnightTour och UserInteraction.

**Chessboard** 
Denna klass representerar brädet och håller koll på brädets tillstånd. Datan lagras i en tvådimensionell lista (board) där varje element representerar en ruta på brädet. 
Klassen ansvarar för att initiera brädet, markera rutor som besökta, visa brädet (grafiskt eller via terminalen) och återställa dess tillstånd. Den hanterar ingen logik för springarens rörelser.

**KnightTour**
Under körningen använder KnightTour temporära variabler för att lagra springarens aktuella position och stegnummer. Den interagerar med Chessboard för att validera och markera drag genom att ta in chessboard objektet som en parameter i sina funktioner.

**UserInteraction**
Klassen UserInteraction fungerar som en brygga mellan användaren och programmets logik. Den kommunicerar med både Chessboard för visa användaren tillståndet på brädet efter varje drag. Men den skickar också användarens input till knightour för att validera giltigheten av drag.