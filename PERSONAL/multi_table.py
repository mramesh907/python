def multi_table(num1:int,num2:int):
    for num in range(1,num2+1):
        print(num1," * ",num," = ",num1*num)
a,b=int(input("Which multiplication table:")),int(input("How many terms:"))
multi_table(a,b)