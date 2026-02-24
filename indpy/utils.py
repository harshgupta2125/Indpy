"""Utility functions for validation algorithms."""

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
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
]

VERHOEFF_P = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
    [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
    [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
    [9, 4, 5, 3, 1, 2, 6, 8, 7, 0],
    [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
    [2, 7, 9, 3, 8, 0, 6, 4, 1, 5],
    [7, 0, 4, 6, 9, 1, 3, 2, 5, 8],
]

VERHOEFF_INV = [0, 4, 3, 2, 1, 5, 6, 7, 8, 9]


def validate_verhoeff(num_str: str) -> bool:
    """Validate Verhoeff checksum for given number string."""
    c = 0
    my_array = list(map(int, reversed(num_str)))
    for i, item in enumerate(my_array):
        c = VERHOEFF_D[c][VERHOEFF_P[i % 8][item]]
    return c == 0


def generate_verhoeff(num_str: str) -> str:
    """Generate Verhoeff checksum digit for given number string."""
    c = 0
    my_array = list(map(int, reversed(num_str)))
    for i, item in enumerate(my_array):
        c = VERHOEFF_D[c][VERHOEFF_P[(i + 1) % 8][item]]
    return str(VERHOEFF_INV[c])


def validate_luhn(card_number: str) -> bool:
    """Validates a number using the Luhn algorithm (Mod 10)."""
    digits = [int(d) for d in str(card_number) if d.isdigit()]
    if not digits:
        return False

    checksum = 0
    is_second = False

    for digit in reversed(digits):
        if is_second:
            digit = digit * 2
            if digit > 9:
                digit -= 9
        checksum += digit
        is_second = not is_second

    return checksum % 10 == 0


def generate_luhn_check_digit(partial_number: str) -> str:
    """Calculates the Luhn check digit for a given partial number."""
    digits = [int(d) for d in str(partial_number) if d.isdigit()]
    if not digits:
        return "0"

    checksum = 0
    is_second = True

    for digit in reversed(digits):
        if is_second:
            digit = digit * 2
            if digit > 9:
                digit -= 9
        checksum += digit
        is_second = not is_second

    return str((10 - (checksum % 10)) % 10)
