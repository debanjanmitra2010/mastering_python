# Highest Score
# Instructions
# You are going to write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Important you are not allowed to use the max or min functions. The output words must match the example. i.e
# The highest score in the class is: x
# Example Input
# 78 65 89 86 55 91 64 89
# In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]
# Example Output
# The highest score in the class is: 91
print("<<<<<<<<<<<<<<< CODED BY DEBANJAN MITRA >>>>>>>>>>>>>>>")

user_choice = int(input("Which method you wanna try (1-without function, 2-using function: "))

if(user_choice == 1):
  #method 1 without using any build in function  
  # Converting Decimal heights to Integer
  student_scores = input("Input a list of student scores ").split()
  for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

  highest_score = 0
  for score in student_scores:
   if(score>highest_score):        
    highest_score = score

  print("The highest score in the class is: ", highest_score)

else:

#   #method 2 using build in function 
  student_scores = input("Input a list of student scores ").split()
  for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
  
  highest_score = max(student_scores)
  print("The highest score in the class is: ", highest_score)
  