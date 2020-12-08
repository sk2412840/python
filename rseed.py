# Program to create a faulty virtual dice
import random

print("Welcome to Dice Simulator")
while True:
    random.seed(9999990)
    dice = random.randint(1, 6)
    print(f"You have got {dice}")
    a= int(input("Do you want to roll again 1\\0 :"))
    if(a==1):
        continue
    else:
        break
print("\nThank You For Playing")
