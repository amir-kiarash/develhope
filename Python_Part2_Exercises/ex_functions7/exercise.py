my_list = [*range(5)]

# Define a lambda function that returns the square of a number if it's even
square_if_even = lambda x: x**2 if x%2 == 0 else x

# Apply the lambda function to each element of my_list using map() function
result = list(map(square_if_even, my_list))

# Print the result to the screen
print(result)