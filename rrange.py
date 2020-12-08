#Program to print a random number between two given numbers
import random

a= int(input("Enter lower limit:\n"))
b= int(input("Enter upper limit:\n"))
b+=1
c= random.randrange(a,b)
print(f"Random number generated is:\n{c}")