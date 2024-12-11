## First L, Honors MV Calc, 12/2024
## Least Squares Project
## Don't forget a breif description of the program in the header!!

## The Numpy module has all the functionality you need to complete this program
import numpy as np

##USEFUL INPUT STUFF
# Just type values in for the simple "data-sets"
dataTypedIn = np.array(
    [[1, 2], [-2, 3], [3, 1], [-5, 5], [4, 2]]
)  # we recommend using numpy arrays instead of just lists
print("Typed-in data:\n", dataTypedIn)

# Eventually you will want to read data from a tab-seperated text file
fname = "sample_data_1.txt"
dataFromFile = np.loadtxt(fname, dtype="float", delimiter="\t")
print("Read-in data:\n", dataFromFile)

# Slicing out just the x or y values into arrays is useful
xVals = dataTypedIn[:, 0]  # Slice out just the x-values
yVals = dataTypedIn[:, 1]  # Slice out just the y-values
print("x-values typed in were : ", xVals)

# Creating empty arrays to put numbers into later is useful
M = np.zeros([4, 3])
print("Empty matrix:\n", M)


##USEFUL CALCULATION STUFF

# Square the elements in xVals (yay for element-wiser operations!!)
xSquared = xVals**2
print("Squares of x-values: ", xSquared)
# Multiply elements in xVals and yVals and sum the products (a dot-product!)
sum_of_x_times_y = sum(xVals * yVals)
print("Sum of products is ", sum_of_x_times_y)

# Loop through matrix M and stick values into it
numRows = len(M[:, 0])
numCols = len(M[0])
print("Dimensions of M: ", numRows, "x", numCols)
for row in range(numRows):
    for col in range(numCols):
        M[row, col] = np.random.randint(-10, 10)  # Just sticking numbers into spots...
print(M)

# Pull out rows 1-3 and cols 1-3 from M to get a square matrix
A = M[0:3, 0:3]
print("A is square:\n", A)

# Multiplying matrices
MtimesA = np.matmul(M, A)
print("M times A:\n", MtimesA)

# Inverting matrices
AInverse = np.linalg.inv(A)
print("Inverse of A:\n", AInverse)
print("(A)(A^-1) should be identity!!\n", np.matmul(A, AInverse))
