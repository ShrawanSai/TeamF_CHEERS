import random

def square(x):
    return (x*x)

def dartBoard(darts):
    score = 0
    for i in range(0, darts):
        xCoord = random.uniform(-1,1)
        yCoord = random.uniform(-1,1)
        xSqr = square(xCoord)
        ySqr = square(yCoord)
        
        if(xSqr + ySqr <= 1):
            score = score + 1

    pi = 4 * (score / darts)
    return pi

def calculate():
    DARTS = 100000
    ROUNDS = 100

    averagePI = 0
    for i in range(0,ROUNDS):
        homePI = dartBoard(DARTS)
        averagePI = ((averagePI * i) + homePI) / (i + 1)

    return averagePI