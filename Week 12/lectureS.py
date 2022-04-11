# cit1113
# Alex Brown
# Lecture S

"""
Arrays and Lists

Lists can be expanded, arrays can't
Lists cn hold multiple types
Python uses lists
"""

kids = ["Alice", "Becky", "Carol"]
for v in kids:
    print("Kid: "+v)

kids[0] = "Ann"
kids[1] = "Bob"
kids[2] = "Chuck"
kids.append("Beans")

for v in kids:
    print("Kid: "+v)

