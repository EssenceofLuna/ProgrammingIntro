# cit1113
# Alex Brown
# Lecture D

def calculatePay(hours, rate):
    #Given hours worked an hourly rate, returns total pay

    pay = hours * rate

    if hours > 40:
        #Add overtime is needed
        overtimeHours = hours - 40
        overtimePay = overtimeHours * rate * 0.5
        pay = pay + overtimePay
    return pay

print(calculatePay(41, 10))