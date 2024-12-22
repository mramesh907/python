def linearsearch(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
arr=[1,2,3,4,5,6,7,8,9,10]
print("The array is:",arr)
key=int(input("Enter the number to be searched:"))
result=linearsearch(arr,key)
if result==-1:
    print("The number is not present in the array")
else:
    print("The number is present at index",result)

