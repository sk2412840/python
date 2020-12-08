import pandas as pd
names = pd.Series(['Ayush', 'Akshay',
                   'Simon', 'Yash',
                   'Naman'])
print("Series you have entered is:")
print(names)
len = names.map(lambda calc: len(calc))
print("No. of characters in each word in the given series:")
print(len)