# using turtle to draw circles

import turtle
t=turtle.Turtle()
t.width (1)
t.speed (0)  # fastest
t.hideturtle()

# move the pen without leaving a line
def relocate (x , y) :
    t.penup()
    t.setx (x)
    t.sety (y)
    t.setheading(90)
    t.pendown()

# draw circle at specified position
def circle ( x ,y , radius , color):
    shiftx = 0
    shifty = 0
    scale = 8
    
    x = scale * (x + shiftx)
    y = scale * (y + shifty)
    radius = radius * scale
    
    relocate (x,y)
    t.color (color , color)
    t.begin_fill()
    t.circle (radius)
    t.end_fill()

# draw crosshairs
def crosshairs(n):
    relocate(0-n/2,0)
    t.setheading(0)
    t.fd(n)
    relocate(0,0-n/2)
    t.setheading(90)
    t.fd(n)

# main
crosshairs( 400 )

# draw tortoise here

# legs
circle(-3, 1.5, 1.25, "yellow") #top left
circle(5, 1.5, 1.25, "yellow") #top right
circle(-3, -6, 1.25, "yellow") #bottom left
circle(5, -6, 1.25, "yellow") #bottom right

# head
circle(2, 5, 2.25, "green")

# eyes
circle(2.5, 5, 0.625, "black")
circle(-2, 5, 0.625, "black")

# pupils
circle(2, 5.5, 0.25, "red")
circle(-2.4, 5.5, 0.25, "red")

# main body
circle(5, -2, 5.25, "black")



# hold program so vscode doesn't close the window
input("Press enter to continue...")