print("*****************************************")
print("Designed by Debanjan")
print("*****************************************")

import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
user_choice = input("Please select which method you wanna try, 1 or 2: ")

if(user_choice == "1"):
    #method1
    num_items = len(names)
    #Generating random numbers between 0 and the last index
    random_choice = random.randint(0, num_items -1)
    pay_person = names[random_choice]
    print(pay_person + " is going to buy the meal today!")

if(user_choice == "2"):
    #method2
    paying_person = random.choice(names)
    print(paying_person + " is going to buy the meal today!")