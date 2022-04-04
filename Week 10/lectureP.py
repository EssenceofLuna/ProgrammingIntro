# cit1113
# Alex Brown
# Lecture P

# lecture N2 - draw a bear
import turtle
t=turtle.Turtle()
t.width (1)
t.speed (0)
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
    shiftx = -40
    shifty = -30
    scale = 8

    x = scale * (x+shiftx)
    y = scale * (y+shifty)
    radius = radius * scale

    relocate (x,y)
    t.color (color , color)
    t.begin_fill()
    t.circle (radius)
    t.end_fill()

# https://trinket.io/docs/colors

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
# circle ( 100, 50, 50, "light blue" )
# circle ( 0, 0, 50, "green" )
# circle ( -100, 0, 100, "orange" )


# your circles go here

# ears
circle(24, 51, 11, "tan")
circle(77, 51, 11, "tan")

# Inner ears
circle(21, 51, 8, "saddle brown")
circle(74, 51, 8, "saddle brown")

# main circle
circle(70, 30, 30, "tan")

# eyes
circle(37, 40, 7.5, "white")
circle(58, 40, 7.5, "white")

# pupils
circle(30, 36, 3, "blue")
circle(51, 36, 3, "blue")

# Nose
circle(48, 27, 8, "saddle brown")

# mouth
circle(44, 14, 4, "black")

# hold program so vscode doesn't close the window
input("Press enter to continue...")