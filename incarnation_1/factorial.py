def factorial(n):
    # Check for negative integer
    if n < 0:
        return None
    # Initialize result variable
    result = 1
    # Iterate from 1 to n
    for i in range(1, n+1):
        try:
            # Multiply each number to the result variable
            result *= i
        except:
            # If there is an error, return None
            return None
    # Return the result variable
    return result
