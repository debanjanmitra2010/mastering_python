print("*****************************************")
print("Designed by Debanjan")
print("*****************************************")

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

playing_person = random.choice(names)
print(playing_person + " is going to buy the meal today!")