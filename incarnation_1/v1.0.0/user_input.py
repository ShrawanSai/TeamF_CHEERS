from decimal import Decimal
from main import Math


def find_alpha():  
    # Function to find the value of alpha using Bisection method
    # Returns the value of alpha as a Decimal object
    
    try: 
        alpha = Math.bisection_solver(0, 10)  # Calling the Bisection method from scratch
        if alpha is None:
            raise ValueError("Alpha cannot be calculated.")
    except Exception as e:
        print(e)
    
    return alpha


def get_radius():  
    # Function to get valid radius input from user
    # Returns the radius as a Decimal object
    while True:
        try:
            r = Decimal(input("Please enter radius: "))
            if r < 0:
                raise ValueError
            return r
        except ValueError:
            print("Invalid Input! radius cannot be less than 0. Please try again")
        except Exception:
            print("Invalid Input! Please enter a correct value (a number)")


def compute_length(radius, alpha):  
    # Function to compute the length of the segment X1X2
    # Returns the length as a Decimal object
    length = 2 * radius * (1 - (Math.cos(alpha / 2)))
    return length


def main():
    
    print("\n\nCustom User input!\n")
    radius = get_radius()  
    alpha = find_alpha()  
    length = compute_length(radius, alpha)  
    
    # Printing the values of alpha and length
    print("Value of Alpha is: {} Radians".format(alpha))
    print("Length of line segement X1X2 is : {}".format(length))
    
    # Writing the values of alpha and length to a file
    with open("output.txt", "a") as file:
        file.write("Value of Alpha is: {} Radians\n".format(alpha))
        file.write("Length of line segement X1X2 is : {}\n".format(length))
        
        
def sample_outputs(sample_radii = [5,10,15,25,50]):
    alpha = find_alpha()  
    print("Value of Alpha is: {} Radians".format(alpha))
    
    for radius in sample_radii:
        length = compute_length(radius, alpha)  
        print("Length of line segement X1X2 when radius is {} = : {}".format(radius,length))
    


if __name__ == '__main__':
    sample_outputs()
    main()
