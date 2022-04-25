# cit1113
# Alex Brown
# Lecture W

"""
Classes

functions in classes are called methods
"""
from math import pi


class Student:
    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.age = 0

s1 = Student()
s1.firstname = "Bob"
s1.lastname = "Roberts"
s1.age = 12

s2 = Student()
s2.firstname = "Rob"
s2.lastname = "Boberts"
s2.age = 13

s3 = Student()
s3.firstname = "Tim"
s3.lastname = "Boberts"
s3.age = 12

L = []
L.append(s1)
L.append(s2)
L.append(s3)

for v in L:
    print(v.firstname, v.lastname, v.age)




print(" ")

# Class for period elements
class Element:
    def __init__(self, symbol = "Null", name = "Null", number = 0, mass = 0):
        self.symbol = symbol
        self.name = name
        self.number = number
        self.mass = float(mass)

    # __str__ will be called if you print the object
    def __str__(self):
        # print(self.symbol, self.name, self.number, self.mass)
        s = "["+str(self.symbol)+"] "+str(self.name)+" | "+str(self.number)+" | "+str(self.mass)
        return s

e1 = Element("H", "Hydrogen", 1, 1.01)
e2 = Element("He", "Helium", 2, 4.0026)

e3 = Element("Li", "Lithium", 3, 6.9410)
e4 = Element("Be", "Beryllium", 4, 9.0122)
e5 = Element("B", "Boron", 5, 10.811)
e6 = Element("C", "Carbon", 6, 12.001)
e7 = Element("N", "Nitrogen", 7, 14.007)
e8 = Element("O", "Oxygen", 8, 15.998)

element_list = [e1, e2, e3, e4, e5, e6, e7, e8]

for v in element_list:
    print(v)




print(" ")

class Sphere:
    def __init__(self, radius):
        self.radius = radius
        self.surfacearea = 4*pi*self.radius**2
        self.volume = (4/3)*pi*self.radius**3

    # Returns a string with rounded values for radius, sa, and volume
    def __str__(self):
        s = "r="+str(round(self.radius, 4))+", sa="+str(round(self.surfacearea, 4))+", v="+str(round(self.volume, 4))
        return s

s1 = Sphere(15)
s2 = Sphere(25)
s3 = Sphere(1024)

sphere_list = [s1, s2, s3]

for v in sphere_list:
    print(v)