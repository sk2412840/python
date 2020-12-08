import re
mystr = """ayush
ayush01
shivam
i am using python flags"""
without_flagM = re.findall(r"^\w+", mystr)
with_flagM = re.findall(r"^\w+", mystr, re.MULTILINE)
print(without_flagM)
print(with_flagM)
