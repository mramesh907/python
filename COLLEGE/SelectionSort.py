# Selection sort in Python
# time complexity O(n*n)
#sorting by finding min_index
def selectionsort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if(arr[j]<arr[min_index]):
                min_index=j
        (arr[i],arr[min_index])=(arr[min_index],arr[i])

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
selectionsort(arr)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
