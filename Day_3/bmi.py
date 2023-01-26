w = float(input("Please enter your weight(kg): "))
h = float(input("Please enter your height(m): "))

BMI = w/(h**2)

print("Your BMI is: ", int(BMI))
if(BMI<18.5):
    print("You are underweight")
elif(BMI>18.5 and BMI<25):
    print("You are normal weight")
elif(BMI>25 and BMI<30):
    print("You are over weight")
elif(BMI>30 and BMI<35):
    print("You are obese")
else:
    print("You are clinically obese")