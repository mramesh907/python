a,b,c=int(input("Enter 1st marks:")),int(input("Enter 2nd marks:")),int(input("Enter 3rd marks:"))
avg=(a+b+c)/3
print("Average of marks is: ",avg)
if(avg>=90):
    print("Grade: A+")
elif(avg>=80 and avg<90):
    print("Grade: A")
elif(avg>=70 and avg<80):
    print("Grade: B")
elif(avg>=60 and avg<70):
    print("Grade: C")
elif(avg>=50 and avg<60):
    print("Grade: D")
elif(avg<50):
    print("Grade: F")

