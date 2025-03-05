# If the entries in A are from Z27, then there are 27**4 possible matrices to choose from. Write a program using any software package to determine how many of these are singular, using your criteria for invertibility above. What percentage of 2×2 matrices are invertible over Z27?

import itertools

# Total number of 2x2 matrices over Z27
total = 27**4
invertible_count = 0

# Iterate over all possible matrices with entries in {0,1,...,26}
for a, b, c, d in itertools.product(range(27), repeat=4):
    # Compute the determinant modulo 27
    det = (a * d - b * c) % 27
    
    # Check if the determinant is a unit in Z27.
    # In Z27, a number is invertible if and only if it is not divisible by 3.
    if det % 3 != 0:
        invertible_count += 1

# Calculate percentage of invertible matrices
percentage_invertible = (invertible_count / total) * 100

print("Total number of matrices:", total)
print("Number of invertible matrices:", invertible_count)
print("Percentage of invertible matrices: {:.2f}%".format(percentage_invertible))


# double check with separate program

import math

def count_invertible_matrices(modulus=27):
    total = modulus ** 4
    count_inv = 0
    for a in range(modulus):
        for b in range(modulus):
            for c in range(modulus):
                for d in range(modulus):
                    det = (a * d - b * c) % modulus
                    # A matrix is invertible if its determinant is a unit in Z27,
                    # i.e. gcd(det, 27) == 1.
                    if math.gcd(det, modulus) == 1:
                        count_inv += 1
    return count_inv, total

if __name__ == '__main__':
    count_inv, total = count_invertible_matrices(27)
    count_sing = total - count_inv
    percentage = (count_inv / total) * 100
    print(f"Total matrices: {total}")
    print(f"Invertible matrices: {count_inv}")
    print(f"Singular matrices: {count_sing}")
    print(f"Percentage invertible: {percentage:.2f}%")
