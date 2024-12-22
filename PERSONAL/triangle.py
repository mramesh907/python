a,b,c=int(input("Enter 1st side:")),int(input("Enter 2nd side:")),int(input("Enter 3rd side:"))
if(a+b>c and a+c>b and b+c>a):
    print("Valid Triangle")
else:
    print("Not a valid Triangle")
