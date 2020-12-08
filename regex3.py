import re
mystr= '''at rat cat mat chat this that
delhi mumbai kolkata lucknow
ayush akshay simon yash naman
'''
x= re.search(r"at", mystr)
y= re.search(r'lucknow',mystr)
z= re.search(r'ayush',mystr)
print(x)
print(y)
print(z)
nf= re.search(r"kanpur",mystr)
print(nf)
