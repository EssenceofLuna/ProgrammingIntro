x = ""
total = 0

print("Enter number to add, or Q to quit")
x = input(">")
while x != "Q":
    x = float(x)
    total = total + x
    print("Enter number to add, or Q to quit")
    x = input(">")

print(total)