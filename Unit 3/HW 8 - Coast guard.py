print("Enter your age.")
age = float(input(">"))

if age < 17:
    print("You are too young to join the coast guard.")
elif age == 17:
    print("You can enlist in the coast guard with permission from your parents.")
elif age >= 18 and age <= 35:
    print("You can enlist in the coast guard.")
elif age >=36 and age <= 40:
    print("You can enlist in the coast guard if you are in the reserves.")
else:
    print("You are too old to join the coast guard.")