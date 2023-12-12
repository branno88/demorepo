
# A simple Python script to calculate Fibonacci sequence

def fibonacci(n):
    '''Return the nth Fibonacci number.'''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test the function
if __name__ == "__main__":
    n = 10  # Change this value to test with different numbers
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
