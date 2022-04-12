# Draw a bear using circles

filename = "circles.txt"

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
    shiftx = -40
    shifty = -30
    scale = 6
    
    # shift and scale
    
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

file = open(filename)

for line in file:
    line = line.strip()  # removes spaces and \n
    if len(line) > 0:
        array = line.split(",")  # convert into array

        # if data does not have four
        # elements (x,y,radius,color)
        # it is not valid, so check.

        if len(array) != 4: 
            print("Bad data", line)
        else:
            # we have good data. 
            # get our drawing values
            # from the array
            x = array[0]
            y = array[1]
            radius = array[2]
            color = array[3]

            # convert data
            x = float(x)
            y = float(y)
            radius = float(radius)
            color = color.strip()
                
            # draw the circle!
            circle(x,y,radius,color) 
        #endif
    #endif
#endfor

file.close()
