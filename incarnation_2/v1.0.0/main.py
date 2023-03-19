import math
from xml.etree.ElementTree import *
        
def bisection_solver(lower_bound:float, upper_bound:float , error_tolerance = 0.5):
    
    """Solves for a root of a non-linear function, given root boundaries and acceptable error"""
    
    # Convert user-entered string to interpretable mathematical function
    
    lower_bound, upper_bound = (lower_bound), (upper_bound)
    
    def compute_alpha(a):  # Initiating the function
        a = (a)
        return a - math.sin(a) - ((math.pi) / 2)

    # Set initial error values
    actual_error = abs(upper_bound - lower_bound)

    # Calculate root using bisection method
    try:
        while actual_error > error_tolerance:
            
                midpoint = (lower_bound + upper_bound) / 2

                if compute_alpha(lower_bound) * compute_alpha(upper_bound) >= 0:
                    raise ValueError("No root present within the given values. Try different values")

                elif compute_alpha(midpoint) * compute_alpha(lower_bound) < 0:
                    upper_bound = midpoint
                    actual_error = abs(upper_bound - lower_bound)

                elif compute_alpha(midpoint) * compute_alpha(upper_bound) < 0:
                    lower_bound = midpoint
                    actual_error = abs(upper_bound - lower_bound)

                else:
                    raise ValueError("Something went wrong. Invalid input")
            
    

        root = (lower_bound + upper_bound) / 2
        return root
    except ValueError as e:
        print(e)
        return None

def find_alpha():  
    # Function to find the value of alpha using Bisection method
    # Returns the value of alpha as a Decimal object
     
    # Exception handling is remaining
    alpha = bisection_solver(0, 10)  # Calling the Bisection method from scratch
    return alpha


def get_radius():  
    # Function to get valid radius input from user
    # Returns the radius as a Decimal object

    # Exception handling is remaining
    r = (int)(input("Please enter radius: "))
    return r

def main():
    
    print("\n\nCustom User input!\n")
    radius = get_radius()  
    alpha = find_alpha()

    # Remaining to compute length


if __name__ == '__main__':
    main()
