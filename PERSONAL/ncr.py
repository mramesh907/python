# Input n and r
n = int(input("Enter value for n: "))
r = int(input("Enter value for r: "))

# Initialize factorial values
n_fact = 1
r_fact = 1
n_minus_r_fact = 1

# Calculating n!
for i in range(1, n + 1):
    n_fact *= i
    if i == r:
        r_fact = n_fact  # Store r! when i equals r
    if i == (n - r):
        n_minus_r_fact = n_fact  # Store (n-r)! when i equals (n-r)

# If r equals 0, set r! and (n-r)! to 1 manually
if r == 0:
    r_fact = 1
    n_minus_r_fact = 1

# Calculate nCr
ncr = n_fact // (r_fact * n_minus_r_fact)

# Output the result
print(f"{n}C{r} = {ncr}")
