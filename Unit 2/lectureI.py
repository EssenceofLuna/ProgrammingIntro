# cit1113
# Alex Brown
# Lecture I

"""
"""

# Donut code

print("Hungry? (Y/N)")
response = input(">")

if response == "Y":
    donuts = 12
    while donuts > 0:
        print("Let's eat a donut!")
        donuts = donuts - 1
        print("Donuts remaining: ", donuts)
else:
    print("Ok, no donuts for you")

print("Done")