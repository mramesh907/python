def palindrom_check(number:int):
	temp=number
	sum=0
	while number > 0:
			rem = number % 10
			sum = sum * 10 + rem
			number=number//10
	if(sum==temp):
		print("The number is a palindrome")
	else:
		print("The number is not palindrome")
number=int(input("Enter number:"))
palindrom_check(number)      
