print("<<<<<<<<<<<<<<< CODED BY DEBANJAN MITRA >>>>>>>>>>>>>>>")
w = float(input("Please enter your weight(kg): "))
h = float(input("Please enter your height(m): "))

BMI = w/(h**2)

if(BMI<18.5):
    print(f"Your BMI is {float(BMI)}, you are underweight.")
elif(BMI>18.5 and BMI<25):
    print(f"Your BMI is {float(BMI)}, you have a normal weight.")
elif(BMI>=25 and BMI<30):
    print(f"Your BMI is {float(BMI)}, you are slightly overweight.")
elif(BMI>=30 and BMI<35):
    print(f"Your BMI is {float(BMI)}, you are obese.")
else:
    print(f"Your BMI is {float(BMI)}, you are clinically obese.")