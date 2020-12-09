import random

def wrongMultiplicationTable(number):
    mul= [number*i for i in range(1,11)]
    wrong= random.randint(1,10)
    mul[wrong]= mul[wrong] + random.randint(1,4)
    return mul

def isCorrect(table,number):
    for i in range(1,11):
        if table[i-1] != number*i:
            return i-1
        
    return None


if __name__ == "__main__":
    
    number= int(input("Enter A Number:\n"))
    table = wrongMultiplicationTable(number)
    print(f"Multiplication Table Of {number} is:\n {table}\n")
    print(f"The Multiplication Table Is Wrong At Index: {isCorrect(table,number)}")
    

    