from graphics import * #imports graphics module

print("""Hello! This is a program that will create a checkerboard.
Please type in the size you want the board to be.""") #introduces user to program and asks user size of board
print(" ") #empty print line for readabillity
sqSz = int(input("Size >>> ")) #waiting for user input of square size (sqSize)
print("Now I will need the color that you would like the board to be.") #asks user color of board (not black tiles)
color = str(input("Color >>> ")) #waiting for user input of color of square (color)

def sq_draw (sqX, sqY, color, size, win): #defining the fuction to draw a square (using x,y coords; color; square size; window)
    square = Rectangle(Point(sqX, sqY), Point(sqX + size, sqY + size)) #points to draw square
    square.setFill(color) #color of the square
    square.draw(chkWin) #draws the actual square

chkWin = GraphWin("Checkers", sqSz * 10, sqSz * 10) #creating the checkers window
chkWin.setCoords(0,0, sqSz * 10, sqSz * 10) #setting the coords of the window

for k in range(8): #the for loop under is repeated 8 times (for each row)
    for i in range(8): 
        if (i + k) % 2 == 0: #if both for loop counters (i and k), when divided, the remainder is 0 set the color
            sqC = color #set the square color to user input
        else: #if remainder is not 0 then
            sqC = "black" #set the square color to black
        sq_draw(sqSz * (i + 1), sqSz * (k + 1), sqC, sqSz, chkWin) #draws square with user color and size

chkWin.getMouse()
chkWin.close()