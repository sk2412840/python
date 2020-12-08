import re
nameage= '''
Ayush is 20 and Akshay is 17
Simon is 13 and Yash is 12
'''
ages= re.findall(r'\d{1,3}',nameage)
names= re.findall(r'[A-Z][a-z]*', nameage)

nameagedict= {}
x=0
for name in names:
    nameagedict[name] = ages[x]
    x+=1
print(nameagedict)


