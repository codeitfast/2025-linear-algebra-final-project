# I was just curious if the fibonacci algorithm or the matrix based algorithm was faster

import timeit

# Iterative addition method (O(n))
def fib_iter(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a + b
    return b

# Helper functions for matrix multiplication and exponentiation
def mat_mult(A, B):
    return [
        [A[0][0]*B[0][0] + A[0][1]*B[1][0],
         A[0][0]*B[0][1] + A[0][1]*B[1][1]],
        [A[1][0]*B[0][0] + A[1][1]*B[1][0],
         A[1][0]*B[0][1] + A[1][1]*B[1][1]]
    ]

def mat_pow(M, n):
    if n == 0:
        # Identity matrix
        return [[1, 0], [0, 1]]
    elif n == 1:
        return M
    elif n % 2 == 0:
        half = mat_pow(M, n // 2)
        return mat_mult(half, half)
    else:
        half = mat_pow(M, n // 2)
        return mat_mult(mat_mult(half, half), M)

# Matrix exponentiation method (O(log n))
def fib_matrix(n):
    if n == 0:
        return 0
    M = [[1, 1], [1, 0]]
    M_n = mat_pow(M, n - 1)
    return M_n[0][0]

# Choose a Fibonacci index to test and number of iterations
n = 1000
iterations = 10000

# Time the iterative method
iter_time = timeit.timeit(lambda: fib_iter(n), number=iterations)
# Time the matrix exponentiation method
matrix_time = timeit.timeit(lambda: fib_matrix(n), number=iterations)

print("fib_iter time:", iter_time)
print("fib_matrix time:", matrix_time)
