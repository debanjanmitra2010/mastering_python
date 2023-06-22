# Adding Evens
# Instructions
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.
print("<<<<<<<<<<<<<<< CODED BY DEBANJAN MITRA >>>>>>>>>>>>>>>")
user_choice = int(input("Which method you wanna try (1, 2): "))
total1 = 0
total2 = 0
if(user_choice == 1):
    for number in range(0,101,2):
        total1 += number
    print("The sum of all even numbers from 0 to 100 is ", total1)

else:
    for number in range(0,101):
        if number % 2 == 0:
            total2 += number
    print("The sum of all even numbers from 0 to 100 is ", total2)


