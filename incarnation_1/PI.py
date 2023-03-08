import random

# method to compute square of X
def square(x):
    return (x*x)

#  subroutine dartboard
#  DESCRIPTION:
    # Used in pi calculation example codes. 
    # To simulate the throwing of darts, 
    # we can generate a large number of random (x, y) coordinates within the square. 
    # We then check whether each point falls inside or 
    # outside the circle by calculating the distance 
    # from the point to the center of the circle, which is (0, 0). 
    # If the distance is less than or equal to the radius of the circle 
    # (which is 1 in this case), then the point is inside the circle.

    # We count the number of points that fall inside the circle 
    # and divide it by the total number of points 
    # to get the ratio of the area of the circle to the area of the square. 
    # We then multiply this ratio by 4 to get an estimate of the value of PI.

    # The dartboard algorithm is based on the fact that 
    # the area of a circle with radius r is given by the formula A = πr^2, 
    # and the area of a square that encloses the circle is given by the formula A = 4r^2. 
    # Therefore, the ratio of the area of the circle to the area of the square is π/4.

#    Explanation of constants and variables used in this function:
#    darts       = number of throws at dartboard
#    score       = number of darts that hit circle
#    xCoord     = x coordinate, between -1 and 1
#    xSqr       = square of x coordinate
#    yCoord     = y coordinate, between -1 and 1
#    ySqr       = square of y coordinate
#    pi          = computed value of pi

def dartBoard(darts):
    score = 0
    
    # Calculates the score for each throw
    for i in range(0, darts):
        xCoord = random.uniform(-1,1)
        yCoord = random.uniform(-1,1)
        xSqr = square(xCoord)
        ySqr = square(yCoord)
        
        # If the throw is on the unit circle or inside the unit circle area
        # then increment score value
        if(xSqr + ySqr <= 1):
            score = score + 1

    # From the score, we get the value of PI/4 value,
    # so multiply by 4 to get the value of PI
    pi = 4 * (score / darts)
    return pi

# method to calculate PI value
def calculate():
    
    # DARTS refers to the number of throws
    # ROUNDS referes to the total number of ROUNDS carried out for better accuracy
    DARTS = 100000
    ROUNDS = 100

    averagePI = 0
    # Calculate average PI for each iteration
    for i in range(0,ROUNDS):
        homePI = dartBoard(DARTS)
        averagePI = ((averagePI * i) + homePI) / (i + 1)
    
    # return the averaged PI, calculated in all the rounds
    return averagePI