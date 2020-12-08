def ispalindrome(n):
    return str(n)==str(n)[::-1]

def nextpalindrome(n):
    n=n+1
    while not ispalindrome(n):
        n=n+1
    return n

if __name__ == '__main__':
    a= int(input("Enter No Of Test Cases:\n"))

    mylist= []

    for i in range(a):
        mylist.append(int(input("Enter A Number:\n")))

    for i in range(a):
        print(f"The Next Palindrome of {mylist[i]} is {nextpalindrome(mylist[i])}\n")


