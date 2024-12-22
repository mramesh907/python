def bubblesort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                (arr[j],arr[j+1])=(arr[j+1],arr[j])

arr = [10,1,14,20,5]
bubblesort(arr)
print('The array after sorting in Ascending Order by bubble sort is:')
print(arr)