# Example Input 1
# B3
# Example Output 1
# Hiding your treasure! X marks the spot.
# ['⬜️', '️⬜️', '️⬜️']
# ['⬜️', '⬜️', '️⬜️']
# ['⬜️️', 'X', '⬜️️']
# Example Input 2
# B1
# Example Output 2
# Hiding your treasure! X marks the spot.
# ['⬜️', 'X', '️⬜️']
# ['⬜️', '⬜️', '️⬜️']
# ['⬜️️', '⬜️️', '⬜️️']

#         A     B     C
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# Your code below
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")