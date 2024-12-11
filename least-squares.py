import numpy as np


def multiplyMatrices(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)


def inverseMatrix(matrix):
    return np.linalg.inv(matrix)


def generateSystemMatrix(degree, xVals):
    numRows = degree + 1
    numCols = degree + 1

    M = np.zeros([numRows, numCols])

    for row in range(numRows):
        for col in range(numCols):
            val = sum(xVals ** ((2 * degree) - (row) - (col)))
            M[row][col] = val

    return M


def generateAnswerMatrix(degree, xVals, yVals):
    numRows = degree + 1
    numCols = 1

    M = np.zeros([numRows, numCols])

    for row in range(numRows):
        for col in range(numCols):
            val = sum((xVals ** (degree - row)) * yVals)
            M[row][col] = val

    return M


def leastSquares():
    fname = "Least-Squares\sample_data_1.txt"
    dataFromFile = np.loadtxt(fname, dtype="float", delimiter="\t")

    xVals = dataFromFile[:, 0]
    yVals = dataFromFile[:, 1]

    degree = int(input("What degree will the polynomial be? "))

    systemMatrix = generateSystemMatrix(degree, xVals)
    inverseSystemMatrix = inverseMatrix(systemMatrix)
    answerMatrix = generateAnswerMatrix(degree, xVals, yVals)

    coefficients = multiplyMatrices(inverseSystemMatrix, answerMatrix)

    print(coefficients)


leastSquares()
