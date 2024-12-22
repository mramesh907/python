def square_list():
    squares = []
    for x in range(1, 31):
        squares.append(x ** 2)
    
    # Combine the first 5 and the last 5 elements
    result = squares[:5] + squares[-5:]
    return result

# Example usage
print(square_list())