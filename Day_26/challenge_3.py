with open("file1.txt") as file1:
  lines = file1.readlines()
  numbers1 = {int(line.strip()) for line in lines}

with open("file2.txt") as file2:
  lines = file2.readlines()
  numbers2 = [int(line.strip()) for line in lines]
  result = [n for n in numbers2 if n in numbers1]

# Write your code above 👆
print(result)