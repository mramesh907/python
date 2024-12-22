import math
a=int(input("Enter number to check perfect square or not:"))
temp=math.sqrt(a)
if(temp*temp==a):
    print(a,"is a perfect square")
else:
    print(a,"is not a perfect square")