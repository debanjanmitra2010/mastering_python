num = [1, 2, 3, 4, 5]
new_nums = [n + 1 for n in num]
print(num)
name = "Debanjan"
letter_list = [letter for letter in name]
print(letter_list)
range_list = [n * 2 for n in range(1,5)]
print(range_list)
names = ["Alex", "Beth", "Debanjan", "Franco", "Dave", "Elina", "Jordan"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
large_names = [name for name in names if len(name) > 5]
print(large_names)
