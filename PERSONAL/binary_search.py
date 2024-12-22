def binary_search(arr, x):
    start = 0  # To track the starting index in the original array
    
    while len(arr) > 0:
        mid = len(arr) // 2
        
        # If the middle element is the target
        if arr[mid] == x:
            return start + mid  # Return the correct index in the original array
        
        # If the target is greater than the middle element, search the right half
        elif arr[mid] < x:
            arr = arr[mid + 1:]  # Slice the right half
            start += mid + 1  # Update the start index to adjust to the new sublist
        
        # If the target is smaller than the middle element, search the left half
        else:
            arr = arr[:mid]  # Slice the left half
    
    return -1  # Return -1 if the element is not found


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
