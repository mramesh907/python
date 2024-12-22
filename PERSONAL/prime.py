def prime_check(num:int):
    flag=False
    if(num>1):
        for i in range(2, num//2+1):
            if (num % i) == 0:
                flag = True
                break
        if flag:
                print(num, "is not a prime number")
        else:
            print(num, "is a prime number")
    else:
        print("You entered 0 or 1 or negative number")
num=int(input("Enter number:"))
prime_check(num)