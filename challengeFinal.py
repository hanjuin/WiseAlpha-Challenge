import random
import os

#Variable#  
grid = []
gridY = []
gridScreen = []
init = 0
shipHit = 0

#Grid Size
gridSize = 8

#Game Round
rd = 20
    
#Create Grid#
for i in range(0,gridSize):
    for j in range(0,gridSize):
        gridY.append(0);
    grid.append(gridY);
    gridY = []

for i in range(0,gridSize):
    for j in range(0,gridSize):
        gridY.append(0);
    gridScreen.append(gridY);
    gridY = []

#Plant ship#
while True:
    ship1X = random.randrange(0,gridSize)
    ship1Y = random.randrange(0,gridSize)
    ship2X = random.randrange(0,gridSize)
    ship2Y = random.randrange(0,gridSize)
    if(ship1X != ship2X and ship1Y != ship2Y):
        break

grid[ship1Y][ship1X] = 1
grid[ship2Y][ship2X] = 1


#Print Grid#
def printScreen():
    print("  ", end = " ")
    for x in range(0, gridSize):
        print(str(x + 1), end = " ")
    print()
    print()
    for i in range(0,gridSize):
        print(str(i+1) + str(" "), end = " ")
        for j in range(0, gridSize):
            if(gridScreen[i][j] == 2):
                 print('S', end=" ")
            elif(gridScreen[i][j] == 3):
                 print('X', end=" ")
            else:
                 print(0, end=" ")
        print()
    print()
    
#Update Screen#
def updateScreen(ipX,ipY):
    if(grid[ipY][ipX] == 1):
        gridScreen[ipY][ipX] = 2
    else:
        gridScreen[ipY][ipX] = 3
       
#Game begin#
print("Battleship Start")
print("1. Enter X and Y Coordinate to hit the ship")
print("2. 'S' in the grid stand for Ship")
print("3. 'X' in the grid stand for Miss")
print("4. You have 20 round, after 20 round if you can't hit two ship, game over")
print()

while(init < rd):
    print("======================================================================")
    if (shipHit < 2):
            
        print("    Round " + str(init+1))
        print()
        printScreen()
        while True:
            x = int(input("Insert X coordinate (Horizontal): "))
            y = int(input("Insert Y coordinate (Vertical): "))
            x = x-1
            y = y-1
            if(x < 0 or y < 0 or x >= gridSize or y >= gridSize):
                print("Invalid Value")
            else:
                break

        updateScreen(x,y)
        print()
        if(grid[y][x] == 1):
            print("--Hit--")
            shipHit += 1
        else:
            d1 = abs(ship1X - x) + abs(ship1Y - y)
            d2 = abs(ship2X - x) + abs(ship2Y - y)

            if(d1 < 2 or d2 < 2):
                print("--Hot--")
            elif((d1 >= 2 and d1 < 4) or (d2 >= 2 and d2 < 4)):
                print("--Warm--")
            else:
                print("--Cold--")
        init += 1
        print()
    else:
        break

if(shipHit < 2):
    print("You lose")
else:
    print("You Win")
    printScreen()
    
print()      
print("Game Over")
print("======================================================================")
