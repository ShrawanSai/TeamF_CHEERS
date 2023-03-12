from decimal import Decimal, getcontext

def factorial(n):
    """Calculate factorial of n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def sin(x):
    """Calculate sin of x with utmost precision."""
    # Set precision to 100 digits
    getcontext().prec = 100

    # Convert x to radians
    x = x * Decimal('0.01745329251994329576923690768')

    # Initialize variables
    result = Decimal('0')
    sign = Decimal('1')

    # Calculate sin(x) using Taylor series
    for i in range(0, 100):
        # Calculate numerator and denominator
        numerator = sign * x ** (2 * i + 1)
        denominator = Decimal(factorial(2 * i + 1))

        # Add term to result
        result += numerator / denominator

        # Update sign for next term
        sign = -sign

    return result

def cos(x):
    """Calculate cos of x with utmost precision."""
    # Set precision to 100 digits
    getcontext().prec = 100

    # Convert x to radians
    x = x * Decimal('0.01745329251994329576923690768')

    # Initialize variables
    result = Decimal('0')
    sign = Decimal('1')

    # Calculate cos(x) using Taylor series
    for i in range(0, 100):
        # Calculate numerator and denominator
        numerator = sign * x ** (2 * i)
        denominator = Decimal(factorial(2 * i))

        # Add term to result
        result += numerator / denominator

        # Update sign for next term
        sign = -sign

    return result

# Test the sin and cos functions with some values

if __name__ == '__main__':
    print(sin(Decimal('0.5')))
    print(cos(Decimal('0.5')))
    print(sin(Decimal('1')))
    print(cos(Decimal('1')))
    print(sin(Decimal('2')))
    print(cos(Decimal('2')))
