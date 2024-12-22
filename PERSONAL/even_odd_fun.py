def even_odd(a:int)-> bool:
    if(a%2==0):
           return True
    else:
           return False
a=int(input("Enter number to check even or odd:"))
if(even_odd(a)):
        print(a," is a even number")
else:
        print(a," is a odd number")
     


