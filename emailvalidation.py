# program for email validation
import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
email= input("Enter your email\n")
if (re.search(regex,email)):
    print("Valid Email")
else:
    print("Invalid Email")




