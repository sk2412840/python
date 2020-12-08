import re
mylist= ["ayush01 ambitious", "ayush01 adaptive", "ayush01 abc", "ayush01 smartworking"
         "ayush01 cr" ]
for element in mylist:
    z= re.match("(a\w+)\W(a\w+)", element)
    if z:
        print((z.groups()))