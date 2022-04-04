# cit1113
# Alex Brown
# Lecture M

"""
else if (elif in python)
"""

# Program to get letter grade based on given percentage
# print("Enter grade 0-100")
# grade = float(input(">"))

# if grade >= 90:
#     print("A")
# elif grade >= 80:
#     print("B")
# elif grade >= 70:
#     print("C")
# elif grade >= 60:
#     print("D")
# else:
#     print("F")

# print("done")

# Function to get letter grade based on given percentage
def getGrade(percent = None, shading = True, getInput = True):

    #Get percent if none given and getInput is true
    if getInput and percent == None:
        print("Enter grade 0-100")
        percent = input(">")

    percent = float(percent)
    
    #set grade to string containing letter grade based on percent
    if shading and percent >= 97:
        grade = "A+"
        gpa = 4.0
    elif shading and (percent >= 92 and percent <= 90):
        grade = "A-"
        gpa = 4.0
    elif percent >= 90:
        grade = "A"
        gpa = 3.7
    
    elif shading and (percent >=87 and percent <= 89):
        grade = "B+"
        gpa = 3.3
    elif shading and (percent >=80 and percent <= 82):
        grade = "B-"
        gpa = 3.0
    elif percent >= 80:
        grade = "B"
        gpa = 2.7

    elif shading and (percent >=77 and percent <= 79):
        grade = "C+"
        gpa = 2.3
    elif shading and (percent >=70 and percent <= 72):
        grade = "C-"
        gpa = 2.0
    elif percent >= 70:
        grade = "C"
        gpa = 1.7

    elif shading and (percent >=67 and percent <= 69):
        grade = "D+"
        gpa = 1.3
    elif percent >= 65:
        grade = "D"
        gpa = 1.0
    
    else:
        grade = "F"
        gpa = 0.0

    #Returns grade as string, gpa as float, and percent as float
    return grade, round(float(percent), 1), float(gpa)

def debugGradeRange(minGrade = 0, maxGrade = 100, shading = True):
    # Function to print out possible grades from getGrade()
    i = minGrade
    for i in range(minGrade, maxGrade + 1):
        print(i, ":", getGrade(i, shading))





# Main function
def main():
    debugGradeRange(-100, 105)
    # grade, percent, gpa  = getGrade()
    # print("Grade: "+grade)
    # print("Percent: "+str(percent)+"%")
    # print("GPA: "+str(gpa))

if __name__ == "__main__":
    main()