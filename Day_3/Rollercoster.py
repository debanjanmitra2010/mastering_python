print("*****************************************")
print("<<<<<<<<<<<<<<< CODED BY DEBANJAN MITRA >>>>>>>>>>>>>>>")
print("*****************************************")
height = int(input("Enter your Height: "))
bill = 0
if(height > 120):
    age = int(input("Enter your Age: "))
    if(age<12):
        bill = 5
        print("You can enjoy the ride by paying $5")
    elif(age>=12 and age<=18):
        bill = 7
        print("You can enjoy the ride by paying $7")
    else:
        bill = 12
        print("You can enjoy the ride by paying $12")
    want_photo = input("Do you want Photo (Y/N) ?")
    if(want_photo == "Y" or "y"):
        bill = bill + 3
        print(f"Your total Bill including Ride and Photo ${bill}")
else:
    print("Sorry you can't take the ride because of your height")