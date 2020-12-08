import re
str= '''Ayush26112000 is a good boy he is studying in srmu lucknow
he is also going ml specialisation from ibm 
'''
r1= re.findall(r"^\w+",str)
print(r1)
r2= re.split(r"\s", str)
print(r2)