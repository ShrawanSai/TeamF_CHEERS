import PI
import trignometric
from decimal import Decimal, getcontext

def bisection(lower_bound, upper_bound, error_tolerance):
    """Solves for a value of alpha, given alpha boundaries and acceptable error"""
    
    # Mathematical function to check for the solution of alpha
    def f(alpha):
        alpha_degree = Decimal(alpha)*Decimal('57.2958')
        return Decimal(alpha) - trignometric.sin(Decimal(alpha_degree)) - Decimal('1.5708') #Decimal(pi_estimator.calculate()/2)

    # Set initial error values
    actual_error = abs(upper_bound - lower_bound)

    # Calculate alpha using bisection method
    try:
        while actual_error > error_tolerance:
            midpoint = (lower_bound + upper_bound) / 2

            if f(lower_bound) * f(upper_bound) >= 0:
                print("No root present within the given values. Try different values")
                return None

            elif f(midpoint) * f(lower_bound) < 0:
                upper_bound = midpoint
                actual_error = abs(upper_bound - lower_bound)

            elif f(midpoint) * f(upper_bound) < 0:
                lower_bound = midpoint
                actual_error = abs(upper_bound - lower_bound)

        root = (lower_bound + upper_bound) / 2
        return root
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

#Testing the bisection method
if __name__ == '__main__':
    pi_estimator = PI.PI()
    print(bisection(2,3,0.001))