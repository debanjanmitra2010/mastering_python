print("<<<<<<<<<<<<<<< CODED BY DEBANJAN MITRA >>>>>>>>>>>>>>>")
yr = int(input("Enter the year you want to test as Leap year: "))
if (yr % 4 == 0):
   if (yr % 100 == 0):
        if (yr % 400 == 0):
            print(f"{yr} is Leap year.")
        else:
            print(f"{yr} is not Leap year.")
   else:
        print(f"{yr} is Leap year.")
else:
    print(f"{yr} is not Leap year.")
