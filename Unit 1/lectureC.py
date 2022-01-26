print("How many time to repeat?")

try:
    repeats = int(input())
except:
    print("Error: invalid input")
    quit()

number = 1
for x in range(repeats):
    print(x, number)
    number = number * 2