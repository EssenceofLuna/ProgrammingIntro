# cit1113
# Alex Brown
# Lecture N

"""
loops

do thing a certain amoutn of time rather than copy-pasting

Definite loops - repeate a specified number of times
Indefinite loops - number of repeats is based on something, not hard coded

loop header - first line of the loop. Has all the info and such
"""

# while loop
x = 1               # initialize
while x <= 10:      # test
    print("while loop: "+str(x))
    x += 1          # update

# similar loop but as a for loop
for x in range(10):
    print("for loop: "+str(x))

"""
while loop went from 1 to 10
for loop went from 0 to 9
same number of loops, but the counter will be 1 different
Be careful about off by 1 errors
"""

# To get for loop to go 1 to 10:
for x in range(1, 11, 1): #start at 1, up to (excluding) 11, step by 1
    print("fixed for loop: "+str(x))