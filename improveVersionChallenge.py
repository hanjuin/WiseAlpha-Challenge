import random

GRID_SIZE = 8
NUMBER_OF_ROUND = 20
NUMBER_OF_SHIP = 2
SHIPS = []

class ship:
    def __init__(self, gridSize,ID):
        self.x = random.randrange(0,gridSize)
        self.y = random.randrange(0,gridSize)
        self.ID = ID
        self.hit = False

    def checkHit(self, inputX, inputY):
        if(self.x == inputX and self.y == inputY):
            self.hit = True
            print("--Ship " + str(self.ID) + " Hit--")
        else:
            d = abs(self.x - inputX) + abs(self.y - inputY)
            if(d < 2):
                print("--Ship " + str(self.ID) + " Warm--")
            elif (d >= 2 and d < 4):
                print("--Ship " + str(self.ID) + " Hot--")
            else:
                print("--Ship " + str(self.ID) + " Cold--")
                
class playboard:
    grid = []
    def __init__(self, gridSize):
        gridY = []
        for i in range(0, GRID_SIZE):
            for j in range(0,GRID_SIZE):
                gridY.append(0)
            self.grid.append(gridY)
            gridY = []

    def updateBoard(self, inputX, inputY, status):
        self.grid[inputY][inputX] =  status
        
    def printBoard(self):
        print("  ", end = " ")
        for x in range(0, GRID_SIZE):
            print(str(x + 1), end = " ")
        print()
        print()
        for i in range(0, GRID_SIZE):
            print(str(i+1) + str(" "), end = " ")
            for j in range(0, GRID_SIZE):
                if(self.grid[i][j] == 2):
                     print('S', end=" ")
                elif(self.grid[i][j] == 3):
                     print('X', end=" ")
                else:
                     print(0, end=" ")
            print()
        print()

def all_shipHit():
    for i in range(0,NUMBER_OF_SHIP):
        if(SHIPS[i].hit == False):
            return False
    return True

def check_input(input):
    try:
        val = int(input)
        return True
    except ValueError:
        return False
      
#Create Ships
def create_ships():
    tempSet = set()
    for i in range(0,NUMBER_OF_SHIP):
        SHIPS.append(ship(GRID_SIZE,i+1))
        tempSet.add((SHIPS[i].x, SHIPS[i].y))
    if (len(tempSet) != NUMBER_OF_SHIP):
        SHIPS.clear()
        create_ships()

#Create Playboard
playBoard = playboard(GRID_SIZE)
create_ships()

#Game begin#
print("Battleship Start")
print("1. Enter X and Y Coordinate to hit the ship")
print("2. 'S' in the grid stand for Ship")
print("3. 'X' in the grid stand for Miss")
print("4. You have 20 round, after 20 round if you can't hit two ship, game over")
print()

while(NUMBER_OF_ROUND != 0):
    print("======================================================================")
    print("    Round " + str(21 - NUMBER_OF_ROUND))
    print()
    playBoard.printBoard()
    while True:
        x = input("Insert X coordinate (Horizontal): ")
        y = input("Insert Y coordinate (Vertical): ")
        if(check_input(x) == True and check_input(y) == True):
            x = int(x)
            y = int(y)
            x = x-1
            y = y-1
            if(x < 0 or y < 0 or x >= GRID_SIZE or y >= GRID_SIZE):
                print("Invalid Value")
            else:
                break
        else:
            print("Wrong Input, please insert integer value.")
    print()
    for i in range(0, NUMBER_OF_SHIP):
        if (SHIPS[i].hit == False):
            SHIPS[i].checkHit(x,y)
            if (SHIPS[i].hit == True):
                playBoard.updateBoard(x,y,2)
                break
            else:
                playBoard.updateBoard(x,y,3)
                
    NUMBER_OF_ROUND -= 1
    if(all_shipHit() == True):
        break
    print()

print()
playBoard.printBoard()    
if(all_shipHit() == True):
    print("You Win")
else:
    print("You Loss")

x = input()
