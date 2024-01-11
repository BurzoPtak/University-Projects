#Simple program that calculates approximation of pi depended on sample number
#Then it compares resuts with Liebniz Formula and pi from numpy

import numpy as np

def MonteCarloMethod(n = 1000,r = 1):
    PointsInCircle = 0
    PointsInSquare = 0
    for i in range(n):
        x = np.random.uniform(0,r)
        y = np.random.uniform(0,r)
        dist = np.sqrt(x**2 + y**2)
        if dist <= r:
            PointsInCircle += 1
        PointsInSquare += 1
    QuarterSquareArea = r**2
    QuarterCircleArea = PointsInCircle/PointsInSquare * QuarterSquareArea
    pi = QuarterCircleArea * 4
    return pi

def LiebnizFormula(n = 1000):
    QuarterPi = 1
    for i in range(1,n):
        if i%2 != 0:
            QuarterPi -= 1/(i+2)
        else:
            QuarterPi += 1/(i+2)
    pi = QuarterPi * 4
    return pi

n = 1000
print(f"Using Monte Carlo method with number of series with n set to {n} pi equals: {MonteCarloMethod(n)}")
print(f"Using Liebniz method with number of series with n set to {n} pi equals: {LiebnizFormula(n)}")
print(f"Value for pi from numpy equals: {np.pi}")

