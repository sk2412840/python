yearage=int(input("Enter YOUR Year/Age:\n"))
if yearage>0 and yearage<150:
    yearage= 2020-yearage
if yearage< 1930:
    print("You Seem To Be The Oldest Person Alive")
    exit()
if yearage> 2020:
    print("You Are Not Yet Born")
    exit()
print(f"You Will Be 100 Year Old in {yearage+100}")
choice= input("Do You Want To Know Your Age In A Particular Year y/n:\n")
if choice== "y":
    opyear= int(input("Enter Year:\n"))
    print(f"You will be {opyear-yearage} in {opyear}")
elif choice== "n":
    print("Thank You")
    exit()
else:
    print("Invalid Input")
    exit()


