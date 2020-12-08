n= int(input("Enter No. Of Apples Ayush Have:\n"))
mn= int(input("Enter Minimum Number Of Students:\n"))
mx= int(input("Enter Maximum Number Of Students:\n"))
if mn==mx:
    print("This is not a valid range")
    exit()
for students in range(mn,mx+1):
    if n%students==0:
        print(f"{students} is a divisor of {n}")
    else:
        print(f"{students} is not a divisor of {n}")



