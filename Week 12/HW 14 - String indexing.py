# Using string indexing, print out all
# the capital letters in this sentence
# fragment.  The first two are done for you.

# print(s[0]) # W
# print(s[5]) # I

s = "When In The Course Of Human Events It Becomes Necessary"

for upper in [char for char in s if char.isupper()]:
    print(upper)