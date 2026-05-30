print("Tresure Island")

print("Your mission is to find the treasure")

choice1=input("left or right? ")

if choice1 =="right":
    print("You fall into a hole. Game Over.")
else:
    choice2= input("swim or wait? ")
    if choice2 =="swim":
        print("you got eaten by a shark. Game Over.")
    else:
        choice3= input("which door? red, blue, or yellow? ")
        if choice3 =="red":
            print("you got burned by fire. Game Over.")
        elif choice3 =="blue":
            print("you got eaten by beasts. Game Over.")
        else:
            print("you found the treasure! You Win!")