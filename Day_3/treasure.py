print("                                         ")
print("*****************************************")
print("Designed by Debanjan")
print("*****************************************")
print("Welcome to Treasure Island \n"
      "Your Mission is to find the tressure")
choice1 = input("Left or Right ? ")
choice2 = ""
choice3 = ""
if choice1[0]=="L" or choice1[0]=="l":
    choice2 = input("swim or wait ? ")
    if choice2[0]=="W" or choice2[0]=="w":
        choice3 = input("Which door ? (Red, Blue, Yellow or Anything) :")
        if choice3[0]=="R" or choice3[0]=="r":
            print("Burned by fire\n"
                "Game Over")
        elif choice3[0]=="B" or choice3[0]=="b":
            print("Eaten by beasts\n"
                "Game Over")
        elif choice3[0]=="Y" or choice3[0]=="y":
            print("You Win!")
        else:
            print("Game Over")
    else: 
     print("Attacked by trout\n"
           "Game Over")
else:
    print("Fall into a hole\n"
          "Game Over")

    
    
