# cit1113
# Alex Brown
# Lecture V



# Slicing a string
s = "DARTH VADER"
print(s[0:5])  # DARTH
print(s[6:11]) # VADER

# Slcing a list
L = [8,7,6,5,3,0,9]
print(L[0:3]) # 8,7,6
print(L[3:])  # 5,3,0,9

# Insert area code (405)
L.insert(0,5)
L.insert(0,0)
L.insert(0,4)

print(L[0:])  # print all 10 numbers

# Formatted string of phone number
phoneNumberString = "("+str(L[0])+str(L[1])+str(L[2])+") "+str(L[3])+str(L[4])+str(L[5])+"-"+str(L[6])+str(L[7])+str(L[8])+str(L[9])
print(phoneNumberString)



import random

# Phone number as a class
class PhoneNumber:
    def __init__(self, area_code = 212, phone_number = 4567890, country_code = 1):
        self.country_code = str(country_code).replace('+', '')
        self.area_code = str(area_code).replace('(', '').replace(')', '')
        self.phone_number = str(phone_number).replace('-', '')

        #self.phoneNumberString = self.country_code+" ("+self.area_code+") "+self.phone_number[0:3]+"-"+self.phone_number[3:10]
        self.updatePhoneNumberString()

    def updatePhoneNumberString(self):
        self.phoneNumberString = self.country_code+"-("+self.area_code+")-"+self.phone_number[0:3]+"-"+self.phone_number[3:10]
    
    def setCountryCode(self, new_country_code = 1):
        new_country_code_string = str(new_country_code).replace('+', '')
        self.country_code = new_country_code_string
        self.updatePhoneNumberString()
        return new_country_code_string

    def setAreaCode(self, new_area_code):
        new_area_code_string = str(new_area_code).replace('(', '').replace(')', '')
        self.area_code = new_area_code_string
        self.updatePhoneNumberString()
        return new_area_code_string

    def setPhoneNumber(self, new_phone_number):
        new_phone_number_string = str(new_phone_number).replace('-', '')
        self.phone_number = new_phone_number_string
        self.updatePhoneNumberString()
        return new_phone_number_string

    def generateRandomNumber(self):
        self.setCountryCode(random.randint(1,9))
        self.setAreaCode(random.randint(100,999))
        self.setPhoneNumber(random.randint(1000000,9999999))
        self.updatePhoneNumberString()



steveNumber = PhoneNumber()
steveNumber.setAreaCode(208)
steveNumber.setPhoneNumber(6771319)
print("Steve: "+steveNumber.phoneNumberString)


lunasNumber = PhoneNumber("((((442)", "-----236--8622")
print("Luna: "+lunasNumber.phoneNumberString)


billysNumber = PhoneNumber(random.randint(100, 999), random.randint(1000000, 9999999))
print("Billy: "+billysNumber.phoneNumberString)
billysNumber.generateRandomNumber()
print("Billy: "+billysNumber.phoneNumberString)