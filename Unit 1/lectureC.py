# Alex Brown
# CIT 1113 Lecture C
# 1/26/2022

# print("How many time to repeat?")

# try:
#     repeats = int(input())
# except:
#     print("Error: invalid input")
#     quit()

# number = 1
# for x in range(repeats):
#     print(x, number)
#     number = number * 2

print("How old are you?")
try:
    age = int(input())
except:
    print("Error: invalid input")
    quit()

months = age * 12
print("You are at least", months, "months old.")
