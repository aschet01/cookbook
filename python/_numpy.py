#!python -i
"""
numpy.py - Recipes using numpy
"""

import numpy as np


# Numpy arrays!
# ndarray stands for N-dimensional array.
a1 = np.array(range(1, 6))
a2 = np.array(range(6, 11))

# Element-wise operations
prod = a1 * a2

# Boolean arrays!
is_even = a1 %2 == 0
# They can be used as indices
evens = a1[is_even]
# evens = a1[a1 % 2 == 0]

# Arrays are homogeneous! These all become strings.
hetero = np.array([1, 'hi', ()])


# 2D arrays!
two_d = np.array([range(1, 6),
                  range(6, 11)])

# Access with double-indexing, or commas
assert two_d[1][1] == two_d[1,1]

# Get dimensions with shape attribute!
assert two_d.shape == (2, 5)

# Broadcast a vector (1D array) onto all rows of a 2D array!
plus_one = two_d + np.array([1] * two_d.shape[1])


# Statistical functions
np.mean(a1)
np.median(a1)
np.std(a1)
np.corrcoef(a1, a2)  # Correlation coefficient matrix

# Extra functions for ndarrays
np.sum(a1)
np.sort(a1)


# Generating data
# Random data
# Set the seed
np.random.seed(31323435)
# Get a random number
rand_num = np.random.rand()  # Float
rand_int = np.random(0, 10)  # in range(0, 10)

# args are: mean, std, count
rands = np.random.normal(5.0, 0.5, 10)
# Round to 2 decimal places
col1 = np.round(rands, 2)

col2 = np.round(np.random.normal(10.0, 0.5, 10), 2)
# Combine arrays as columns of a new array
new_array = np.column_stack((col1, col2))
