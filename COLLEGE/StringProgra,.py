def count_same_string():
    str=['aba','abba','abc','abca','abab']
    cout=0
    for i in str:
        if len(i)>=2 and i[0]==i[-1]:
            cout+=1
    print(cout)
# count_same_string()

def multiply_items():
    list=[1,2,3,4,5]
    result=1
    for i in list:
        result=result*i
    print(result)
# multiply_items()

def remove_duplicates():
    list=[1,2,3,4,5,5,4,3,2,1]
    result=[]
    for i in list:
        if i not in result:
            result.append(i)
    print(result)
# remove_duplicates()

def check_empty_list():
    list=[1,2,3]
    if not list:
        print('List is empty')
    else:
        print('List is not empty')
# check_empty_list()

def common_items():
    list1=[1,2,3,4,5]
    list2=[5,6,7,8,9]
    result=list(set(list1) & set(list2))
    print(result)
# common_items()

def square():
    result=[]
    for i in range(1,31):
        result.append(i**2)
    show=result[:5]+result[-5:]
    print(show)
# square()

def list_to_string():
    list=['I','am','a','student']
    # result=' '.join(list)
    result=''
    for i in list:
        result=result+i+' '
    print(result)
list_to_string()

def pattern1():
    n=int(input('Enter a number:'))
    for i in range(1,n+1):
        print(' '*(n-i),end="")
        for j in range(1,i+1):
            print(j,end="")
        for j in range(i-1,0,-1):
            print(j,end="")
        print()
# pattern1()

def even_odd():
    list=[1,2,3,4,5,6,7,8,9,10]
    even=[]
    odd=[]
    for i in list:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print(even)
    print(odd)
# even_odd()

def multiplication_table():
    a=int(input('Enter a number:'))
    for i in range(1,11):
        print(a,'*',i,'=',a*i)
# multiplication_table()

import math
def armstrong():
    num=int(input("Enter number:"))
    temp1=temp2=num
    count=0
    res=0
    while(temp1>0):
        temp1=temp1//10
        count+=1
    while(temp2>0):
        rem=temp2%10
        res=res+math.pow(rem,count)
        temp2=temp2//10
    if(res==num):
        print(num,"is an Armstrong number")
    else:
        print(num,"is not an Armstrong number")
# armstrong()

def palindrom():
    n=int(input('Enter a number:'))
    temp=n
    sum=0
    while(n>0):
        rem=n%10
        sum=sum*10+rem
        n=n//10
    if(temp==sum):
        print('The number is a palindrome')
    else:
        print('The number is not a palindrome')
# palindrom()

def check_prime():
    start,end=int(input('Enter a start number:')),int(input('Enter a end number:'))
    for n in range(start,end):
        if n>1:
            for i in range(2,int(math.sqrt(n))+1):
                if n%i==0:
                    print(n,'is not a prime number')
                    break
            else:
                print(n,'is a prime number')
        else:
            print(n,'is not a prime number')
# check_prime()

def repeted_items():
    s=input('Enter a string:')
    common_items=[]
    count=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1
        else:
            if count>1:
                common_items.append(s[i-1]+str(count))
            count=1
    if count>1:
        common_items.append(s[-1]+str(count))
    print(common_items)
# repeted_items()

def largest_word():
    s=input('Enter a string:')
    words=s.split()
    big=words[0]
    for i in words:
        if len(i)>len(big):
            big=i
    print(big)
# largest_word()

def reverse_string():
    s=input('Enter a string:')
    print('Reversed string:',' '.join(reversed(s.split())))
# reverse_string()

def check_substring():
    s=input('Enter a string:')
    sub=input('Enter a substring:')
    if sub in s:
        print('Substring found')
    else:
        print('Substring not found')
# check_substring()

def string_palindrome():
    s=input('Enter a string:')
    if s==s[::-1]:
        print('String is a palindrome')
    else:
        print('String is not a palindrome')
# string_palindrome()

def convert_to_upper():
    s=input('Enter a string:')
    print('Upper case string:',s.upper())
# convert_to_upper()

def replace_character():
    s=input('Enter a string:')
    char=input('Enter a character:')
    new_char=input('Enter a new character:')
    print('Replaced string:',s.replace(char,new_char))
# replace_character()

def count_upper():
    s=input('Enter a string:')
    count=0
    for i in s:
        if i.isupper():
            count+=1
    print('Number of uppercase characters:',count)
# count_upper()

def count_words():
    s=input('Enter a string:')
    words=s.split()
    print('Number of words:',len(words))
# count_words()

def length_of_string():
    s=input('Enter a string:')
    length=0
    for char in s:
        length+=1
    print('Length of string:',len(s))
# length_of_string()

def sum_of_digits():
    a,b=int(input('Enter a number:')),int(input('Enter a number:'))
    sum=a+b
    print('Sum of digits:',sum)
# sum_of_digits()

def reverse_number():
    n=int(input('Enter a number:'))
    rev=0
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    print('Reversed number:',rev)
# reverse_number()

def grade_calculator():
    marks=int(input('Enter a marks:'))
    if marks>=90:
        print('Grade A+')
    elif marks>=80 and marks<90:
        print('Grade A')
    elif marks>=70 and marks<80:
        print('Grade B')
    elif marks>=60 and marks<70:
        print('Grade C')
    elif marks>=50 and marks<60:
        print('Grade D')
    else:
        print('Grade F')
# grade_calculator()

def valid_triangle():
    a,b,c=int(input('Enter a number:')),int(input('Enter a number:')),int(input('Enter a number:'))
    if a+b>c and b+c>a and c+a>b:
        print('The triangle is valid')
    else:
        print('The triangle is not valid')
# valid_triangle()

import math
def perfect_square():
    n=int(input('Enter a number:'))
    temp=math.sqrt(n)
    if(temp*temp==n):
        print(n,'is a perfect square')
    else:
        print(n,'is not a perfect square')
# perfect_square()

def largest_number():
    a,b,c,d=int(input("Enter 1st number:")),int(input("Enter 2nd number:")),int(input("Enter 3rd number:")),int(input("Enter 4th number:"))
    big=a
    if(b>big):
        big=b
    elif(c>big):
        big=c
    elif(d>big):
        big=d
    print(big," is largest number")
# largest_number()

def leap_year():
    year=int(input("Enter a year:"))
    if(year%4==0 and year%100!=0 or year%400==0):
        print(year," is leap year")
    else:
        print(year," is not leap year")
# leap_year()