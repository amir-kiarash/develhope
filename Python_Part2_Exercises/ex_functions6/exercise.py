def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

# Print the first 5 elements of the Fibonacci sequence
for i in range(5):
    print(fibonacci(i))