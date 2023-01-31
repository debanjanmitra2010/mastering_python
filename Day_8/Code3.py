# Prime Numbers
# Instructions
# Prime numbers are numbers that can only be cleanly divided by itself and 1.
# https://en.wikipedia.org/wiki/Prime_number
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime n'umber because you can divide it by 1, 2 or 4.
# Cannot infer image mime type
# Here are the numbers up to 100, prime numbers are highlighted in yellow:
# Cannot infer image mime type
# Example Input 1
# 73
# Example Output 1
# It's a prime number.
# Example Input 2
# 75
# Example Output 2
# It's not a prime number.

user_choice = int(input("Do you want to just check a prime number or see it in a range: \n" 
                        "Press 1 for prime check \n"
                        "Press 2 for Prime Number in Range \n "
                        "Your Choice: "))


def prime_number(num):
    count = 0
    for i in range(1, num+1):
        if(num % i == 0):
            count +=1 
    if count == 2:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
        

if(user_choice ==1): 
    num = int(input("Please enter the number you want to check for prime number: "))       
    prime_number(num)

if(user_choice ==2): 
    n = int(input("Enter the Range upro which youn want to print Prime Numbers: "))
    for i in range(1, n):
        prime_number(i)