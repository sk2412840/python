import random

print("Welcome To Number Guessing Game")
lower= int(input("Enter Lower Limit:\n"))
upper= int(input("Enter Upper Limit:\n"))
rnum1= random.randint(lower,upper)
rnum2= random.randint(lower,upper)
na = 0
nb = 0

print("\nPlayer A Start Playing\n")
while True:
    a = int(input("Guess A Number:\n"))
    if a == rnum1:
        na = na + 1
        break
    elif a > rnum1:
        print("Guess A Smaller One")
        na = na+1
        continue
    elif a < rnum1:
        print("Guess A Greater One")
        na = na + 1
        continue
    else:
        print("An Error Accured")
        exit()

print("\nPlayer B Start Playing\n")
while True:
    b = int(input("Guess A Number\n"))
    if b == rnum2:
        nb = nb + 1
        break
    elif b > rnum2:
        print("Guess A Smaller One")
        nb = nb+1
        continue
    elif b < rnum2:
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
elif na == nb:
    print("Its A Tie")
else:
    exit()

print(f"The Number For Player A Is: {rnum1}\n")
print(f"The Number For Player B Is: {rnum2}\n")

print("Thank You For Playing")
