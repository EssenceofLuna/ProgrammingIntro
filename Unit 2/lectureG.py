# cit1113
# Alex Brown
# Lecture G

"""
use = to set
use == to compare

= is called the assignment operator

garbage is a variable with no value. declared but not set.



constant variables - doesn't change while program is running.
All caps for names used to denote them

# c family
const int MAX_FILES = 20;

# java
final string path = "C:/temp"

P
E
MD
AS

Abstraction - selective ignorance. Focus on main idea and ignore details.
"""

from time import sleep
import turtle

leo = turtle.Turtle()

def shape(sides = 4, length = 100, left = False):
    # sides - number of sides of shape - high numbers will look like circles
    # length - length of sides
    # left - if true, direction turtle turns is inverted

    # if no values given, a square of length 100 is drawn

    angle = 360 / sides


    x = 1
    while x <= sides:
        leo.forward(length)
        if (left == False): leo.right(angle)
        else: leo.left(angle)

        x = x + 1
    

# Main function
def main():
    leo.speed(10) # speed of turtle (0-100)
    num_shapes = 36 # Number of shapes to be drawn around (0,0)


    for x in range(num_shapes):
        shape()
        leo.right(360/num_shapes)

    sleep(4) # sleep at end to see result. Not needed if using IDLE.


# run main()
if __name__ == "__main__":
    main()

# old, ignore
#leo.fd(100)
#leo.right(90)
#leo.fd(100)