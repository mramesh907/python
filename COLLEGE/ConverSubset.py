def subset(s, size):
    result = []
    
    def generate(index, curr):
        # If current subset size matches the desired size, add it to the result
        if len(curr) == size:
            result.append(curr[:])  # Use curr[:] to create a copy of the list
            return
        
        # Recursively generate subsets by choosing each element once
        for i in range(index, len(s)):
            generate(i + 1, curr + [s[i]])  # Add element and move to the next index
    
    # Start the recursion with an empty subset and index 0
    generate(0, [])
    
    return result

# Example usage
s = [1, 2, 3, 4]
size = 2
print(subset(s, size))
