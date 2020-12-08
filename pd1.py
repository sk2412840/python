import pandas as pd
sr1= pd.Series([1,5,9,7,2])
sr2= pd.Series([5,7,22,3,9])
choice= int(input("Enter your choice:\n "
                  "1- add\n "
                  "2- subtract\n "
                  "3- multiply\n "
                  "4- divide\n "
                  "5- modulus\n "))
if(choice==1) :
    sr3= sr1+sr2
elif choice==2:
    sr3= sr1-sr2
elif choice==3:
    sr3= sr1*sr2
elif choice==4:
    sr3= sr1/sr2
elif choice==5:
    sr3= sr1%sr2
print(sr3)












































































