import random
class PI:
    """
        A Class that uses simulation of throwing of darts to calculate an estimate of PI.
    """


    def __init__(self):
        """
            a special method in Python classes that is called when an instance of the class is created. 
            It allows you to initialize the attributes of the object and perform any other necessary setup.
        """
        pass


    def _square(self, x):
        """Compute the square of x."""
        return x ** 2


    def _dart_board(self, darts):
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
            x_sqr = self._square(x_coord)
            y_sqr = self._square(y_coord)
            # If the throw is on the unit circle or inside the unit circle area
            # then increment score value
            if x_sqr + y_sqr <= 1:
                score += 1
        # From the score, we get the value of PI/4 value,
        # so multiply by 4 to get the value of PI
        pi = 4 * (score / darts)
        return pi


    def calculate(self):
        """
            Calculate the value of pi.
            Where we run the dartboard algorithm number of times to get better accuracy.
        """
        # DARTS refers to the number of throws
        # ROUNDS refers to the total number of rounds carried out for better accuracy.
        DARTS = 100_000
        ROUNDS = 100
        average_pi = 0
        # Calculate average pi for each iteration
        for i in range(ROUNDS):
            home_pi = self._dart_board(DARTS)
            average_pi = ((average_pi * i) + home_pi) / (i + 1)
        # return the averaged pi, calculated in all the rounds
        return average_pi