print("*****************************************")
print("Designed by Debanjan")
print("*****************************************")
num1 = input("Enter any number: ")
sum1 = 0

num2 = input("Enter a two digit number only: ")
sum2 = 0

#Method2 for a two digit number only 
if(len(num2)==2):
    first_digit = num2[0]
    second_digit = num2[1]
    sum2 = sum2 + int(first_digit) + int(second_digit)
else:
    print("Not a two digit number")


#Method1
for digits in num1:
    sum1 = sum1 + int(digits)

print("Result from first method 1 ",sum1)
print("Result from first method 2 ",sum2)
print(len(num2))