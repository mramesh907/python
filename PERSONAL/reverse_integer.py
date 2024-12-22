number=int(input("Enter number:"))
temp=number
sum=0
while number > 0:
		rem = number % 10
		sum = sum * 10 + rem
		number=number//10

print("Original Number:",temp)
print("Reversed Number:",sum)
