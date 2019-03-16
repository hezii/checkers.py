from graphics import * #imports graphics module

sqX = 0 #inti variable
sqY = 0 #inti variable

print("""Hello! This is a program that will create a checkerboard.
Please type in the size you want the board to be.""") #introduces user to program and asks user size of board
print(" ") #empty print line for readabillity
sqSz = int(input("Size >>> ")) #waiting for user input of square size (sqSize)

chkWin = GraphWin("Checkers", sqSz * 10, sqSz * 10) #creating the checkers window
chkWin.setCoords(0,0, sqSz * 10, sqSz * 10) #setting the coords of the window

square = Rectangle(Point(sqX, sqY), Point(sqX + sqSz, sqY + sqSz)) #points to draw square
square.setFill("black") #color of the square
square.draw(chkWin) #draws the actual square

chkWin.getMouse()
chkWin.close()