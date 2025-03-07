import numpy as np
from sympy import Matrix
import random

def is_invertible_mod_27(A):
    det = int(round(np.linalg.det(A))) % 27
    return det != 0 and np.gcd(det, 27) == 1

def generate_random_matrix():
    return np.array([[random.randint(0, 26) for _ in range(3)] for _ in range(3)])

def calculate_invertible_percentage(trials=100000):
    invertible_count = 0
    
    for i in range(trials):
        A = generate_random_matrix()
        if is_invertible_mod_27(A):
            invertible_count += 1
    
    return (invertible_count / trials) * 100

# Run the experiment
percentage_invertible = calculate_invertible_percentage()
print(f"Percentage of invertible 3x3 matrices in Z_27: {percentage_invertible:.2f}%")
