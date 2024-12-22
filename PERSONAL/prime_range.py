# Get the range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Prime numbers between {start} and {end} are:")

# Loop through the range
for num in range(start, end + 1):
    if num > 1:  # Only check numbers greater than 1
        is_prime = True
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
