# cit1113
# Alex Brown
# Lecture D

"""
def calculatePay(hours, rate):
    #Given hours worked an hourly rate, returns total pay

    pay = hours * rate

    if hours > 40:
        #Add overtime is needed
        overtimeHours = hours - 40
        overtimePay = overtimeHours * rate * 0.5
        pay = pay + overtimePay
    return pay

print("Enter hours worked")
hours = float(input(">"))
print("Enter hourly rate")
rate = float(input(">"))

print(calculatePay(hours, rate))"""





#Get hours worked and rate of pay
print("Enter hours worked this week")
hours = float(input(">"))

print("Enter hourly rate")
rate = float(input(">"))

#Calculate base pay rate
pay = hours * rate

#Add overtime pay
if hours > 40:
    pay = pay + (hours-40) * 0.5

print("Pay: ", pay)