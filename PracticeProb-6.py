import random

print("Welcome To Number Guessing Game")
lower= int(input("Enter Lower Limit:\n"))
upper= int(input("Enter Upper Limit:\n"))
rnum= random.randint(lower,upper)
na = 0
nb = 0

print("\nPlayer A Start Playing\n")
while True:
    a = int(input("Guess A Number:\n"))
    if a == rnum:
        na = na + 1
        break
    elif a > rnum:
        print("Guess A Smaller One")
        na = na+1
        continue
    elif a < rnum:
        print("Guess A Greater One")
        na = na + 1
        continue
    else:
        print("An Error Accured")
        exit()

print("\nPlayer B Start Playing\n")
while True:
    b = int(input("Guess A Number\n"))
    if b == rnum:
        nb = nb + 1
        break
    elif b > rnum:
        print("Guess A Smaller One")
        nb = nb+1
        continue
    elif b < rnum:
        print("Guess A Greater One")
        nb = nb + 1
        continue
    else:
        print("An Error Occured")
        exit()

print(f"\nPlayer A Took {na} Attempts To Guess A Number")
print(f"Player B Took {nb} Attempts To Guess A Number")

if nb > na:
    print("\nPlayer A Won\n")
elif na > nb:
    print("\nPlayer B Won\n")
else:
    exit()

print("Thank You For Playing")
