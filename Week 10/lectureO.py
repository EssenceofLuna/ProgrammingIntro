# cit1113
# Alex Brown
# Lecture O

"""
Nested loops
Example: clocks
"""

hour = 1
while hour < 7:
    minute = 0
    while minute < 60:
        print(hour, minute)
        minute += 15
    hour += 1

# Same loop but as for loops
for hour in range(1,7,1):
    for minute in range(0,60,15):
        print(hour, minute)

"""
Pre-test and post-test loops
while and for are pre-test
Python doesn't have a post-test loop

All loops can be written using while loops
"""