print("*****************************************")
print("<<<<<<<<<<<<<<< CODED BY DEBANJAN MITRA >>>>>>>>>>>>>>>")
print("*****************************************")
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is her name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower() 

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

first_digit = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

second_digit = l + o + v + e

love_score = int(str(first_digit) + str(second_digit))

if (love_score < 10) or (love_score > 90):
  print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}")
   