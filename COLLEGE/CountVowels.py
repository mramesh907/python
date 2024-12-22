def count(str):
    str=str.lower()
    vowels=set("aeiou")
    return len([char for char in str if char in vowels])
str="Hello World"
print(count(str))