#lecture O

# declarations
counter = 1
total = 0
nums = 0
nums_add = 0

print("Add how many numbers?")
nums = int(input(">"))

if nums < 0:
    print("Error")
    print("Cannot add a negative # of numbers")

# Old loop
# while counter <= nums:
#     print("Enter number", counter)
#     num_add = int(input(">"))
#     total = total + num_add
#     counter = counter + 1

for i in range(1, nums+1, 1):
    print("Enter number", i)
    num_add = int(input(">"))
    total += num_add

print("Total =", total)