"""Mock data generators for testing."""

import random
import string
from .utils import generate_verhoeff, generate_luhn_check_digit


class Generate:
    """Generate valid mock Indian document numbers."""

    @staticmethod
    def pan() -> str:
        """Generate valid PAN card number."""
        prefix = "".join(random.choices(string.ascii_uppercase, k=3))
        suffix = random.choice(string.ascii_uppercase)
        digits = "".join(random.choices(string.digits, k=4))
        return f"{prefix}P{random.choice(string.ascii_uppercase)}{digits}{suffix}"

    @staticmethod
    def tan() -> str:
        """Generates a random valid TAN number."""
        first_four = "".join(random.choices(string.ascii_uppercase, k=4))
        digits = "".join(random.choices(string.digits, k=5))
        last_char = random.choice(string.ascii_uppercase)
        return first_four + digits + last_char

    @staticmethod
    def dl() -> str:
        """Generates a random Indian Driving License number."""
        state = random.choice(["MH", "DL", "KA", "UP", "TN", "GJ", "WB"])
        rto = f"{random.randint(1, 99):02d}"
        year = str(random.randint(1990, 2024))
        number = "".join(random.choices(string.digits, k=7))
        return state + rto + year + number

    @staticmethod
    def mobile() -> str:
        """Generate valid Indian mobile number."""
        start = random.choice("6789")
        rest = "".join(random.choices(string.digits, k=9))
        return f"{start}{rest}"

    @staticmethod
    def vehicle() -> str:
        """Generate valid vehicle registration number."""
        state = random.choice(["DL", "UP", "MH", "KA", "TN", "HR"])
        dist = f"{random.randint(1, 99):02}"
        series = "".join(random.choices(string.ascii_uppercase, k=2))
        num = f"{random.randint(1, 9999):04}"
        return f"{state}{dist}{series}{num}"

    @staticmethod
    def aadhaar() -> str:
        """Generate valid Aadhaar number with Verhoeff checksum."""
        first = random.choice("23456789")
        middle = "".join(random.choices(string.digits, k=10))
        base_11 = first + middle
        checksum = generate_verhoeff(base_11)
        return base_11 + checksum

    @staticmethod
    def voterid() -> str:
        """Generate valid Voter ID (EPIC) number."""
        letters = "".join(random.choices(string.ascii_uppercase, k=3))
        digits = "".join(random.choices(string.digits, k=7))
        return letters + digits

    @staticmethod
    def passport() -> str:
        """Generate valid Passport number."""
        letter = random.choice(string.ascii_uppercase)
        digits = "".join(random.choices(string.digits, k=7))
        return letter + digits

    @staticmethod
    def cin() -> str:
        """Generate valid Corporate Identity Number."""
        ownership = random.choice(["L", "U"])
        industry = "".join(random.choices(string.digits, k=5))
        state = "".join(random.choices(string.ascii_uppercase, k=2))
        year = str(random.randint(2000, 2024))
        type_code = random.choice(["PTC", "PLC", "OPC", "GOI"])
        registration = "".join(random.choices(string.digits, k=6))
        return f"{ownership}{industry}{state}{year}{type_code}{registration}"

    @staticmethod
    def pincode() -> str:
        """Generate valid Indian pincode."""
        first = random.randint(1, 9)
        rest = "".join(random.choices(string.digits, k=5))
        return f"{first}{rest}"

    @staticmethod
    def credit_card() -> str:
        """
        Generates a random, valid 16-digit credit card number.
        Defaults to a Visa format (starts with 4).
        """
        partial = "4" + "".join(random.choices(string.digits, k=14))
        check_digit = generate_luhn_check_digit(partial)
        return partial + check_digit
