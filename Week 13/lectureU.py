# cit1113
# Alex Brown
# Lecture U

"""
.append - add item to list
"""


"""
nums = []

x = input("Enter number to add, or Q to quit >")
while x != "Q":
    x = float(x)
    nums.append(x)
    print("Data =", nums)
    x = input("Enter number to add, or Q to quit >")

total = sum(nums)
if len(nums) == 0:
    average = 0
else:
    average = total / len(nums)

print("total =", total)
print("average =", average)
"""





import random
import statistics

how_many = int(input("How many random numbers in list? >"))


random_nums = []
for i in range(how_many):
    n = random.randint(1, 1000)
    random_nums.append(n)


# total = sum(random_nums)
# if len(random_nums) == 0:
#     average = 0
# else:
#     average = total / len(random_nums)

print("total =", sum(random_nums))
# print("average =", average)
print("mean =", statistics.mean(random_nums))
print("median =", statistics.median(random_nums))
# print("mode =", statistics.mode(random_nums))
print("Std Dev =", round(statistics.stdev(random_nums), 3))

random_nums.sort()
print(random_nums)