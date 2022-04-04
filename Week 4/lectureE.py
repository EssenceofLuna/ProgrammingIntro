# cit1113
# Alex Brown
# Lecture E

# Lecture notes:
"""
hexed.it - view hexadecimal code

input - things coming in
output - things going out
application - does a thing
"""



# pseudocode
"""
start
    input myNumber
    set myAnswer = myNumber * 2
    output myAnswer
stop
"""
# in-class code
"""
print("Enter a number to double:")
myNumber = float(input(">"))

myAnswer = myNumber * 2

print("Doubled number:", myAnswer)
"""

# My enhanced code
try:
    print("Enter a number to double:")
    myNumber = float(input(">"))
except:
    print("Error: invalid number entered.")
    quit()

myAnswer = myNumber * 2

print("Doubled number:", myAnswer)