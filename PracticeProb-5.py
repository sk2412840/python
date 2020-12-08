def ispalindrome(n):
    return str(n)==str(n)[::-1]

def nextpalindrome(n):
    n=n+1
    while not ispalindrome(n):
        n=n+1
    return n

if __name__ == "__main__":
    size=int(input("Enter List Size:\n"))
    num_list= []
    for element in range(size):
        num_list.append(int(input("Enter A Number:\n")))
    new_list=[]
    for element in num_list:
        if element<10:
            new_list.append(element)
        else:
            new_list.append(nextpalindrome(element))
    print(f"The List You Have Entered Is:\n {num_list}")
    print(f"The List Of Next Palindromes Is:\n {new_list}")


