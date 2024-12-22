# *
# **
# ***
# ****
# 'end' specifies waht to print at the end of the output,instead of the default newline('\n').


def print_star(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
n=int(input("Enter how many rows:"))
print_star(n)