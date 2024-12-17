"""
Least Squares Polynomial Approximation Generator
Authors: Kellan W, Kira M, Natalie B

Relevant information:
This program takes in a dataset of (x,y) coordinate pairs, then uses matrices to produce a polynomial of best fit.
The "System Matrix" represents each variable & coefficient for the system of equations.
The "Answer Matrix" represents each output value / answer for each system of equations.

There are n equations for a given system, where n is the degree of the target polynomial plus one. This is because
there is always one more coefficient than the degree of the polynomial (e.g. 2nd degree: Ax^2 + Bx + C), and you
always need the same amount of equations as you have variables to solve a system of equations.

Due to the fact that each "cell" in the matrices below contains terms equal to the amount of datapoints,
approximations for larger datasets (e.g. sample_data_4 with 2000 datapoints) will output different coefficient values
depending on the processing power of the computer it is running on.

For small datasets, you can only approximate to a polynomial degree LESS than the number of datapoints present.
This is because there is simply not enough information to generate a specific line of best fit, since there are
technically infinite curves that will pass through every single datapoint perfectly.
"""

# Code begins!!
import numpy as np


# Defines a function for multiplying matrices for better readability later
def multiplyMatrices(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)


# Defines a function for generating the inverse of a matrix for better readability later
def inverseMatrix(matrix):
    return np.linalg.inv(matrix)


# Defines a function to generate the matrix representing the variable terms in the system of equations
def generateSystemMatrix(degree, xVals):
    # The size of this matrix will always be degree+1 x degree+1
    numRows = degree + 1
    numCols = degree + 1

    # Create a placeholder matrix M full of zeros
    M = np.zeros([numRows, numCols])

    # Nested for loop to iterate through each matrix "cell" once
    for row in range(numRows):
        for col in range(numCols):
            # Using numpy, we can evaluate long strings of terms at a given set of X values using one operation
            val = sum(xVals ** ((2 * degree) - (row) - (col)))
            M[row][col] = val

    return M


# Defines a function to generate the matrix representing the answer terms in the system of equations
def generateAnswerMatrix(degree, xVals, yVals):
    # There exists one answer (row in answer matrix) for each equation (row in system matrix)
    numRows = degree + 1
    # But only one column. numCols could be replaced with 1 below since it is constant, but it is kept as a variable for consistency.
    numCols = 1

    # Create a placeholder matrix M full of zeros
    M = np.zeros([numRows, numCols])

    # Nested for loop to iterate through each matrix "cell" once
    # Not strictly necessary since [for col in range(1)] only ever runs once, but kept for consistency
    for row in range(numRows):
        for col in range(numCols):
            # Using numpy, we can evaluate for a given set of X values and a given set of Y values with one operation
            val = sum((xVals ** (degree - row)) * yVals)
            M[row][col] = val

    return M


# Main program function
def leastSquares():
    # Load data from txt file
    fname = "[INSERT_NAME_OF_FILE_IN_SAME_DIRECTORY].txt"
    dataFromFile = np.loadtxt(fname, dtype="float", delimiter="\t")

    # Define a numpy array for every X value in our dataset
    xVals = dataFromFile[:, 0]
    # Define a numpy array for every Y value in our dataset
    yVals = dataFromFile[:, 1]

    # User input
    degree = int(input("What degree will the polynomial be? "))
    print()

    # Generate matrices
    systemMatrix = generateSystemMatrix(degree, xVals)
    inverseSystemMatrix = inverseMatrix(systemMatrix)
    answerMatrix = generateAnswerMatrix(degree, xVals, yVals)

    # Generate polynomial coefficients
    coefficients = multiplyMatrices(inverseSystemMatrix, answerMatrix)

    # Print out the coefficients & the equation
    equation = ""
    for i in range(len(coefficients)):
        coefficient = round(coefficients[i][0], 7)
        print(chr(97 + i) + ": " + str(coefficient))
        if i != degree:
            equation += "(" + str(coefficient) + ")x^" + str(degree - i) + " + "
        else:
            equation += "(" + str(coefficient) + ")"

    print("\n" + equation + "\n")


# Run the program!
leastSquares()
