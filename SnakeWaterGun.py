import random
import sys

choicelist= ["Snake", "Water", "Gun"]

player= input("Enter s for Snake, w for Water or g for Gun :\n")
if player== "s":
    player= "Snake"
elif player== "w":
    player= "Water"
elif player== "g":
    player= "Gun"
else:
    print("Invalid Input")
    sys.exit()

if player in choicelist:
    computer= random.choice(choicelist)
    if player== "Snake" and computer== "Snake":
        print(f"Your Choice is {player} and computer's choice is {computer}")
        print("It's a Draw")
    elif player== "Snake" and computer== "Water":
        print(f"Your Choice is {player} and computer's choice is {computer}")
        print("You Win")
    elif player== "Snake" and computer== "Gun":
        print(f"Your Choice is {player} and computer's choice is {computer}")
        print("Computer Win")
    elif player == "Water" and computer == "Snake":
        print(f"Your Choice is {player} and computer's choice is {computer}")
        print("Computer Win")
    elif player == "Water" and computer == "Water":
        print(f"Your Choice is {player} and computer's choice is {computer}")
        print("It's a Draw")
    elif player == "Water" and computer == "Gun":
        print(f"Your Choice is {player} and computer's choice is {computer}")
        print("You Win")
    elif player == "Gun" and computer == "Snake":
        print(f"Your Choice is {player} and computer's choice is {computer}")
        print("You Win")
    elif player == "Gun" and computer == "Water":
        print(f"Your Choice is {player} and computer's choice is {computer}")
        print("Computer Win")
    elif player == "Gun" and computer == "Gun":
        print(f"Your Choice is {player} and computer's choice is {computer}")
        print("It's a Draw")
    else:
        sys.exit()




