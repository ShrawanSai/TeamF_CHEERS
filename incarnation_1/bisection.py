class bisection:
    def __init__(self, func, lower_bound, upper_bound, error_tolerance):
        """
            a special method in Python classes that is called when an instance of the class is created. 
            It allows you to initialize the attributes of the object and perform any other necessary setup.
        """
        self.func = func
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.error_tolerance = error_tolerance

    def solve(self):
        """Solves for a root of a non-linear function, given root boundaries and acceptable error"""
        # Convert user-entered string to interpretable mathematical function
        def f(x):
            return eval(self.func)

        # Set initial error values
        actual_error = abs(self.upper_bound - self.lower_bound)

        # Calculate root using bisection method
        while actual_error > self.error_tolerance:
            midpoint = (self.lower_bound + self.upper_bound) / 2

            if f(self.lower_bound) * f(self.upper_bound) >= 0:
                print("No root present within the given values. Try different values")
                return None

            elif f(midpoint) * f(self.lower_bound) < 0:
                self.upper_bound = midpoint
                actual_error = abs(self.upper_bound - self.lower_bound)

            elif f(midpoint) * f(self.upper_bound) < 0:
                self.lower_bound = midpoint
                actual_error = abs(self.upper_bound - self.lower_bound)

            else:
                print("Something went wrong")
                return None

        root = (self.lower_bound + self.upper_bound) / 2
        return root