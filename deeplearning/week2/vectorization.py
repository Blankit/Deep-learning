import time
import numpy as np
x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]
x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]

def un_vectorization(x1,x2):
    ### CLASSIC DOT PRODUCT OF VECTORS IMPLEMENTATION ###
    tic = time.time()
    dot = 0
    for i in range(len(x1)):
        dot += x1[i] * x2[i]
    toc = time.time()
    print ("dot = " + str(dot) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")

    ### CLASSIC OUTER PRODUCT IMPLEMENTATION ###
    tic = time.time()
    outer = np.zeros((len(x1), len(x2)))  # we create a len(x1)*len(x2) matrix with only zeros
    for i in range(len(x1)):
        for j in range(len(x2)):
            outer[i, j] = x1[i] * x2[j]
    toc = time.time()
    print ("outer = " + str(outer) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")

    ### CLASSIC ELEMENTWISE IMPLEMENTATION ###
    tic = time.time()
    mul = np.zeros(len(x1))
    for i in range(len(x1)):
        mul[i] = x1[i] * x2[i]
    toc = time.time()
    print ("elementwise multiplication = " + str(mul) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")

    ### CLASSIC GENERAL DOT PRODUCT IMPLEMENTATION ###
    W = np.random.rand(3, len(x1))  # Random 3*len(x1) numpy array
    tic = time.time()
    gdot = np.zeros(W.shape[0])
    for i in range(W.shape[0]):
        for j in range(len(x1)):
            gdot[i] += W[i, j] * x1[j]
    toc = time.time()
    print ("gdot = " + str(gdot) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")


def vectorization(x1,x2):
    x1 = np.array(x1)
    x2 = np.array(x2)
    ###  DOT PRODUCT OF VECTORS IMPLEMENTATION ###
    tic = time.time()
    dot = np.dot(x1,x2)
    toc = time.time()
    print ("dot = " + str(dot) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")

    ### OUTER PRODUCT IMPLEMENTATION ###
    tic = time.time()
    outer = np.outer(x1,x2)
    toc = time.time()
    print ("outer = " + str(outer) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")

    ###  ELEMENTWISE IMPLEMENTATION ###
    tic = time.time()
    mul = x1*x2
    toc = time.time()
    print ("elementwise multiplication = " + str(mul) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")

    ### GENERAL DOT PRODUCT IMPLEMENTATION ###
    W = np.random.rand(3, len(x1))  # Random 3*len(x1) numpy array
    tic = time.time()
    gdot = np.dot(W,x1)
    toc = time.time()
    print ("gdot = " + str(gdot) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")


un_vectorization(x1,x2)
print '*'*10
vectorization(x1,x2)