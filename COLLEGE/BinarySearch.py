def binarysearch(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return -1
arr=[1,2,3,4,5,6,7,8,9,10]
print("The array is:",arr)
key=int(input("Enter the number to be searched:"))
result=binarysearch(arr,key)
if result==-1:
    print("The number is not present in the array")
else:
    print("The number is present at index",result)