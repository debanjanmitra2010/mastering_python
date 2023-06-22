print("*****************************************")
print("<<<<<<<<<<<<<<< CODED BY DEBANJAN MITRA >>>>>>>>>>>>>>>")
print("*****************************************")
age = int(input("Please enter your age: "))
days = age * 365
weeks = age * 52 
months = age * 12
days_left = (90*365) - days
weeks_left = (90*52) - weeks
months_left = (90*12) - months

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left")