import time
from math import factorial

import numpy as np
from scipy.special import factorial as scipy_factorial

# Create a large array for testing
test_array = np.arange(0, 20)

# Implementation 1: np.vectorize
def vectorize_factorial(array):
    vec_factorial = np.vectorize(factorial)
    return vec_factorial(array)

# Implementation 2: scipy.special.factorial
def scipy_factorial_implementation(array):
    return scipy_factorial(array, exact=True)

# Implementation 3: Custom numpy loop
def custom_factorial(array):
    result = np.ones_like(array, dtype=int)
    for i in range(1, array.max() + 1):
        result[array >= i] *= i
    return result

# Measure execution time
times = {}

# Time np.vectorize
start = time.time()
for i in range(1000):
    vectorize_factorial(test_array)
times['np.vectorize'] = time.time() - start

# Time scipy.special.factorial
start = time.time()
for i in range(1000):
    scipy_factorial_implementation(test_array)
times['scipy.special.factorial'] = time.time() - start

# Time custom implementation
start = time.time()
for i in range(1000):
    custom_factorial(test_array)
times['custom_factorial'] = time.time() - start

print(times)
