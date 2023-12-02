height = int(input("Enter your Height: "))
if(height > 120):
    age = int(input("Enter your Age: "))
    if(age<12):
        print("You can enjoy the ride by paying $5")
    elif(age>=12 and age<=18):
        print("You can enjoy the ride by paying $7")
    else:
        print("You can enjoy the ride by paying $12")
else:
    print("Sorry you can't take the ride because of your height")