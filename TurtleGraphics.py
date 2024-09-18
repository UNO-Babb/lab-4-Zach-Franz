#TurtleGraphics.py
#Name: Zachary Franzluebbers
#Date: 9/18/24
#Assignment: Turtle graphics

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(myTurtle, sides):
    for i in range(sides):
        myTurtle.forward(50)
        myTurtle.right(360/sides)
    
    


    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon


def fillCorner(myTurtle, corner):
    drawSquare(myTurtle, 100) #square of size 100
    if corner == 1:
        myturtle.goto(0,0)
        
    elif corner == 2:
        myTurtle.goto(50,0)
        
    elif corner == 3:
        myTurtle.up()
        myTurtle.goto(50,-50)
        myTurtle.down()
        
    elif corner == 4:
        myTurtle.goto(0,-50)
    
    myTurtle.begin_fill()
    drawSquare(myTurtle, 50)
    myTurtle.end_fill()
    

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

   
    
def squaresInSquares(myTurtle, number):
    size = 100
    y = 0
    x = 0
    for i in range(number):
        myTurtle.down()
        drawSquare(myTurtle, size)
        size = size - 10
        y = y - 5
        x = x + 5
        myTurtle.up()
        myTurtle.goto(x, y)
        
    
        
    
    
    
    
    
def main():
    myTurtle = turtle.Turtle()
    
    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares

main()
