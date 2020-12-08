import pandas as pd
sr = pd.Series([5,6,7,9,22,37,69])
print("Pandas Series and it's type")
print(sr)
print(type(sr))
print("Converting Pandas Series to Python list")
print(sr.to_list())
print(type(sr.to_list()))
