# File: indpy/utils.py

# Verhoeff Algorithm Tables
# Source: Official logic for Aadhaar checksums

# Table D: The multiplication table
VERHOEFF_D = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
    [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
    [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
    [4, 0, 1, 2, 3, 9, 5, 6, 7, 8],
    [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
    [6, 5, 9, 8, 7, 1, 0, 4, 3, 2],
    [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
    [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
]

# Table P: The permutation table
VERHOEFF_P = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
    [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
    [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
    [9, 4, 5, 3, 1, 2, 6, 8, 7, 0],
    [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
    [2, 7, 9, 3, 8, 0, 6, 4, 1, 5],
    [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]
]

# Table INV: The inverse table
VERHOEFF_INV = [0, 4, 3, 2, 1, 5, 6, 7, 8, 9]

def validate_verhoeff(num_str):
    """Checks if the 12-digit number has a valid checksum."""
    c = 0
    # Reverse the number to process from right to left
    my_array = list(map(int, reversed(num_str)))
    
    for i, item in enumerate(my_array):
        c = VERHOEFF_D[c][VERHOEFF_P[i % 8][item]]
    
    return c == 0

def generate_verhoeff(num_str):
    """Calculates the 12th digit (checksum) for the first 11 digits."""
    c = 0
    my_array = list(map(int, reversed(num_str)))
    
    for i, item in enumerate(my_array):
        c = VERHOEFF_D[c][VERHOEFF_P[(i + 1) % 8][item]]
        
    return str(VERHOEFF_INV[c])