# cit1113
# Alex Brown
# Lecture T

"""
Parallel arrays
Same length, items are linked by subscript #
"""

from asyncio.windows_events import NULL


a1 = ["red", "blue", "green"]
a2 = ["apples", "berries", "beans"]
a3 = [1.99, .99, 2.99]

for i in range(len(a1)):
    print(a1[i], a2[i], a3[i])

"""
Classes
"""

class Student:
    def __init__(self, name = "NULL",  gpa = -1, address = "NULL"):
        self.name = name
        self.address = address
        self.gpa = float(gpa)
        
        self.previousNames = []
        self.previousAddresses = []
        self.completedCourses = []
        

    def setAddress(self, address):
        if self.address != "NULL":
            self.previousAddresses.append(self.address)
        self.address = address

    def setName(self, name):
        if self.name != "NULL":
            self.previousNames.append(self.name)
        self.name = name

    def addCompletedCourse(self, course_name):
        self.completedCourses.append(course_name)

    def setGPA(self, gpa):
        self.gpa = gpa

    def updateDetails(self, name = "NULL", gpa = -1, address = "NULL"):
        if name != "NULL":
            self.setName(name)
        if gpa != -1:
            self.setGPA(gpa)
        if address != "NULL":
            self.setAddress(address)

    def printDetails(self):
        print("Student name:", self.name)
        print("GPA:", self.gpa)
        print("Student address:", self.address)

        if len(self.previousNames) > 0:
            print("Previous Names:", self.previousNames)
        if len(self.previousAddresses) > 0:
            print("Previous addresses:", self.previousAddresses)
        if len(self.completedCourses) > 0:
            print("Completed Courses:", self.completedCourses)


students = [Student("Jess Johnson", 2), Student("Steve Koinm", 2.3), Student("Fred Kennedy", 3.2), Student("NULL", 99.99)]

def printAllStudentDetails():
    for i in students:
        i.printDetails()


students[0].printDetails()

students[0].setAddress("1234 Street Road")
students[0].setAddress("5678 Rainbow Road")
students[0].setAddress("555 Mulberry Street")
students[0].printDetails()

students[0].addCompletedCourse("C++")
students[0].addCompletedCourse("Java")
students[0].addCompletedCourse("English Comp I")
students[0].addCompletedCourse("English Comp II")
students[0].addCompletedCourse("College Algebra")
students[0].addCompletedCourse("Chemistry Intro")
students[0].printDetails()

students[0].updateDetails("Luna Johnson", -1, "9507 Place Ave.")
students[0].printDetails()