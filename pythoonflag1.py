import re

mystr = """Good Morning All
My name is Ayush Kumar
And i am from Lucknow
"""

without_S = re.findall(r".+", mystr)
with_S = re.findall(r".+", mystr, re.S)

print(without_S)

print(with_S)
