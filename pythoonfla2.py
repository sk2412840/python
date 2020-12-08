import re

mystr = """good Morning All
My name is Ayush Kumar
And i am from Lucknow
"""

without_I = re.findall(r"^\w+[A-Z][a-z]", mystr)
with_I = re.findall(r"^\w+[A-Z][a-z]", mystr, re.I)

print(without_I)

print(with_I)
