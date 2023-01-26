print("Welcome to the tip calculator")
bill = float(input("What was the total bill ? "))
tip = int(input("What % tip would you like to give ? 10,12, or 15 ? "))
ppl = int(input("How many people to split the bill ? "))

each_ppl = (bill * (100+tip)) / (100*ppl)
final_amount = round(each_ppl, 2)
print("Each person should pay: ", final_amount)