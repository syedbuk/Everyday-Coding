import random




print("Welcome to Rock Paper Scissors")

list_of_symbols=["Rock", "Paper", "Scissors"]




choice = int(input("What do you choose? Type  0 for rock, 1 for paper, or 2 for Scissors: "))
computer_choice= random.randint(0,2)

print(f"You chose {list_of_symbols[choice]}")

print(f"Computer chose {list_of_symbols[computer_choice]}")

if choice == computer_choice:
    print("its a draw")
elif choice==0 and computer_choice==1:
    print("you win")
elif choice==1 and computer_choice==2:
    print("you win")
elif choice==2 and computer_choice==0:
    print("you win")
else:
    print("you lose")




