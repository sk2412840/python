size= int(input("Enter Total No. Of Food Items:\n"))
print("Enter Calories One By One\n")
calories= []
for i in range(size):
    calories.append(int(input("Enter Calorie:\n")))
print(f"\nOriginal Calorie List: {calories}")
reverse1= calories[:]
reverse1.reverse()
print(f"First Reverse List is {reverse1}")
reverse2= calories[::-1]
print(f"Second Reverse List is {reverse2}")
reverse3= calories[:]
for i in range(size//2):
    reverse3[i],reverse3[size-i-1]= reverse3[size-i-1], reverse3[i]
print(f"Third Reverse List is {reverse3}")

if reverse1==reverse2 and reverse2==reverse3:
    print("\n All Three Reversed Lists Are Same\n")
