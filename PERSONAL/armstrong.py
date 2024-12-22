import math
def check_armstrong(num:int):
    temp1=temp2=num
    count=0
    res=0
    while(temp1>0):
        temp1=temp1//10
        count+=1
    while(temp2>0):
        rem=temp2%10
        res=res+math.pow(rem,count)
        temp2=temp2//10
    if(res==num):
        print(num,"is an Armstrong number")
    else:
        print(num,"is not an Armstrong number")
num=int(input("Enter number:"))
check_armstrong(num)