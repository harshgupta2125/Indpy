"""
Module for generating dummy data for testing purposes.
Useful for QA and Development environments.
"""

import random
import string
from .utils import generate_verhoeff

class Generate:
    @staticmethod
    def pan() -> str:
        """Generates a syntactically valid random PAN card number."""
        # Structure: 3 Random chars + 'P' + Random char + 4 Random Digits + 1 Random Char
        prefix = ''.join(random.choices(string.ascii_uppercase, k=3))
        digits = ''.join(random.choices(string.digits, k=4))
        suffix = random.choice(string.ascii_uppercase)
        
        return f"{prefix}P{random.choice(string.ascii_uppercase)}{digits}{suffix}"

    @staticmethod
    def mobile() -> str:
        """Generates a random Indian mobile number starting with 6-9."""
        start = random.choice(['6', '7', '8', '9'])
        rest = ''.join(random.choices(string.digits, k=9))
        return f"{start}{rest}"

    @staticmethod
    def vehicle() -> str:
        """Generates a random DL/UP style vehicle number."""
        state = random.choice(['DL', 'UP', 'MH', 'KA', 'TN', 'HR'])
        dist = f"{random.randint(1, 99):02}" # Pads with 0 if needed
        series = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
        num = f"{random.randint(1, 9999):04}"
        return f"{state}{dist}{series}{num}"

    @staticmethod
    def aadhaar() -> str:
        """
        Generates a random valid Aadhaar number with correct Verhoeff checksum.
        Ensures it does not start with 0 or 1.
        """
        # Generate first digit (2-9)
        first = random.choice(['2', '3', '4', '5', '6', '7', '8', '9'])        
        # Generate next 10 digits
        middle = ''.join(random.choices(string.digits, k=10))
        
        # Calculate the checksum digit using Verhoeff algorithm
        base_11 = first + middle
        checksum = generate_verhoeff(base_11)
        
        return base_11 + checksum