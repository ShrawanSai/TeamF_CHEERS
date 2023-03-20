from decimal import Decimal, getcontext
import random
import pickle
# Set precision to 100 digits for precise answers
getcontext().prec = 100


class Math:
    """
        A Class that returns the Math functions: Sine, Cosine, Factorial.
    """

    @staticmethod
    def _abs(value: float) -> float:
        """Function to return absolute value"""

        if value >= 0:
            return value
        else:
            return value*-1

    @staticmethod
    def _powerof(base: float, exponent: int) -> float:
        """Calculates power of the given base and exponent"""
        
        result = 1
        if exponent == 0:
            return result
        elif exponent < 0:
            base = 1/base
            exponent = -exponent
        for i in range(1, exponent+1):
            result *= base
        return result

    @staticmethod
    def _dart_board(darts: int) -> float:
        """
        Simulate the throwing of darts to calculate an estimate of pi.

        Generate a large number of random (x, y) coordinates within a square.
        Check whether each point falls inside or outside a circle with a radius of 1.
        Count the number of points that fall inside the circle and divide it by the total number of points
        to get the ratio of the area of the circle to the area of the square.
        Multiply this ratio by 4 to get an estimate of the value of pi.
        """
        score = 0
        # Calculates the score for each throw
        for i in range(darts):
            x_coord = random.uniform(-1, 1)
            y_coord = random.uniform(-1, 1)
            x_sqr = Math._powerof(x_coord, 2)
            y_sqr = Math._powerof(y_coord, 2)
            # If the throw is on the unit circle or inside the unit circle area
            # then increment score value
            if x_sqr + y_sqr <= 1:
                score += 1
        # From the score, we get the value of PI/4 value,
        # so multiply by 4 to get the value of PI
        pi = 4 * (score / darts)
        return pi

    @staticmethod
    def get_pi(ROUNDS=1000) -> float:
        """
            Calculate the value of pi.
            Where we run the dartboard algorithm number of times to get better accuracy.
        """
        # DARTS refers to the number of throws
        # ROUNDS refers to the total number of rounds carried out for better accuracy.
        DARTS = 100_000
        if ROUNDS == 1000:
            try:
                with open("pi_at_1000_rounds.pkl", "rb") as file:
                    return pickle.load(file)
            except (FileNotFoundError, EOFError, pickle.UnpicklingError):
                pass

        average_pi = 0
        # Calculate average pi for each iteration
        for i in range(ROUNDS):
            home_pi = Math._dart_board(DARTS)
            average_pi = ((average_pi * i) + home_pi) / (i + 1)
        # return the averaged pi, calculated in all the rounds

        # Saving value of pi it was calculated at 1000 rounds
        if ROUNDS == 1000:
            try:
                with open("pi_at_1000_rounds.pkl", "wb") as file:
                    pickle.dump(average_pi, file)
            except Exception:
                pass
        return average_pi

    @staticmethod
    def factorial(n: int) -> int:
        """Calculate factorial of n."""
        try:
            # Check for negative integer
            if n < 0:
                raise ValueError("Factorial not defined for negative numbers")
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
        except ValueError as e:
            print(e)
            return None

    @staticmethod
    def sin(x: float) -> Decimal:
        """Compute the sine of x using a Taylor series expansion"""

        try:
            # Convert x to radians
            x = Decimal(x)
            x = x * Decimal('0.01745329251994329576923690768')

            # Initialize variables
            result = Decimal('0')
            sign = Decimal('1')

            # Calculate sin(x) using Taylor series
            for i in range(0, 100):
                # Calculate numerator and denominator
                numerator = sign * Math._powerof(x, 2 * i + 1)
                denominator = Decimal(Math.factorial(2 * i + 1))

                # Add term to result
                result += numerator / denominator

                # Update sign for next term
                sign = -sign

            return result

        except ValueError:
            print("Invalid input for sin() function")

    @staticmethod
    def cos(x: float) -> Decimal:
        """Compute the cosine of x using a Taylor series expansion"""
        try:
            # Convert x to radians
            x = Decimal(x)
            x = x * Decimal('0.01745329251994329576923690768')

            # Initialize variables
            result = Decimal('0')
            sign = Decimal('1')

            # Calculate cos(x) using Taylor series
            for i in range(0, 100):
                # Calculate numerator and denominator
                numerator = sign * Math._powerof(x, 2 * i + 1)
                denominator = Decimal(Math.factorial(2 * i))

                # Add term to result
                result += numerator / denominator

                # Update sign for next term
                sign = -sign

            return result
        except ValueError:
            print("Invalid input for cos() function")

    @staticmethod
    def bisection_solver(lower_bound: float, upper_bound: float, error_tolerance=0.5) -> Decimal:
        """Solves for a root of a non-linear function, given root boundaries and acceptable error"""

        # Convert user-entered string to interpretable mathematical function

        lower_bound, upper_bound = Decimal(lower_bound), Decimal(upper_bound)

        def compute_alpha(a):  # Initiating the function
            a = Decimal(a)
            return a - Math.sin(a) - (Decimal(Math.get_pi()) / 2)

        # Set initial error values
        actual_error = Math._abs(upper_bound - lower_bound)

        # Calculate root using bisection method
        try:
            while actual_error > error_tolerance:

                midpoint = (lower_bound + upper_bound) / 2

                if compute_alpha(lower_bound) * compute_alpha(upper_bound) >= 0:
                    raise ValueError(
                        "No root present within the given values. Try different values")

                elif compute_alpha(midpoint) * compute_alpha(lower_bound) < 0:
                    upper_bound = midpoint
                    actual_error = Math._abs(upper_bound - lower_bound)

                elif compute_alpha(midpoint) * compute_alpha(upper_bound) < 0:
                    lower_bound = midpoint
                    actual_error = Math._abs(upper_bound - lower_bound)

                else:
                    raise ValueError("Something went wrong. Invalid input")

            root = (lower_bound + upper_bound) / 2
            return root
        except ValueError as e:
            print(e)
            return None


if __name__ == '__main__':
    print(Math.sin(0.5))
    print(Math.cos(0.5))
    print(Math.get_pi())
    print(Math.factorial(4))
    print(Math.factorial(-44))
    # Random numbers given just to check the result
    print(Math.bisection_solver(5, 500))
