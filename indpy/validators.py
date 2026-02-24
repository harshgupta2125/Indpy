"""Core validation logic for Indian Identity and Financial documents."""

import re
from typing import Iterable, Optional
from .utils import validate_verhoeff, validate_luhn

PATTERNS = {
    "pan": re.compile(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"),
    "mobile": re.compile(r"^[6-9]\d{9}$"),
    "ifsc": re.compile(r"^[A-Z]{4}0[A-Z0-9]{6}$"),
    "credit_card": re.compile(r"^\d{13,19}$"),
    "vehicle": re.compile(r"^[A-Z]{2}[0-9]{1,2}[A-Z]{0,3}[0-9]{4}$"),
    "upi": re.compile(r"^[\w\.\-]+@[\w\.\-]+$"),
    "voterid": re.compile(r"^[A-Z]{3}[0-9]{7}$"),
    "passport": re.compile(r"^[A-Z][0-9]{7}$"),
    "cin": re.compile(r"^[LU]\d{5}[A-Z]{2}\d{4}[A-Z]{3}\d{6}$"),
    "pincode": re.compile(r"^[1-9]\d{5}$"),
}


def is_pan(pan_number: str) -> bool:
    """
    Validates Permanent Account Number (PAN).

    Regex: ^[A-Z]{5}[0-9]{4}[A-Z]{1}$
    - ^[A-Z]{5}    : Starts with exactly 5 uppercase letters
    - [0-9]{4}     : Followed by exactly 4 digits
    - [A-Z]{1}     : Ends with 1 uppercase letter
    - $            : End of string

    Example: ABCDE1234F
    Usage: is_pan("ABCDE1234F") -> True
    """
    if not isinstance(pan_number, str):
        return False
    return bool(PATTERNS["pan"].match(pan_number.upper()))


def is_mobile(number: str) -> bool:
    """
    Validates 10-digit Indian mobile number.

    Regex: ^[6-9]\\d{9}$
    - ^[6-9]       : Starts with digit 6, 7, 8, or 9 (not 0-5)
    - \\d{9}       : Followed by exactly 9 digits (0-9)
    - $            : End of string

    Accepts: Spaces, dashes, +91 prefix (automatically removed)
    Example: 9876543210 or +91-9876543210 or 9876-543210
    Usage: is_mobile("9876543210") -> True
    """
    if not number:
        return False
    clean_num = str(number).replace(" ", "").replace("-", "").replace("+91", "")
    return bool(PATTERNS["mobile"].match(clean_num))


def is_ifsc(code: str, valid_bank_codes: Optional[Iterable[str]] = None) -> bool:
    """
    Validates Indian Financial System Code (IFSC).

    Regex: ^[A-Z]{4}0[A-Z0-9]{6}$
    - ^[A-Z]{4}    : Starts with exactly 4 uppercase letters (bank code)
    - 0            : 5th character must be literal '0'
    - [A-Z0-9]{6}  : Followed by 6 alphanumeric characters (branch code)
    - $            : End of string

    Format: AAAA0XXXXXX (11 characters total)
    Example: SBIN0004321
    Usage: is_ifsc("SBIN0004321") -> True

    Optional: pass valid_bank_codes to enforce known bank codes.
    """
    if not code:
        return False

    clean_code = str(code).replace(" ", "").upper()
    if not PATTERNS["ifsc"].match(clean_code):
        return False

    if valid_bank_codes is not None:
        bank_code = clean_code[:4]
        if bank_code not in {str(c).upper() for c in valid_bank_codes}:
            return False

    return True


def is_vehicle(number: str) -> bool:
    """
    Validates RC (Registration Certificate) number.

    Regex: ^[A-Z]{2}[0-9]{1,2}[A-Z]{0,3}[0-9]{4}$
    - ^[A-Z]{2}    : Starts with 2 uppercase letters (state code)
    - [0-9]{1,2}   : Followed by 1 or 2 digits (district code)
    - [A-Z]{0,3}   : 0 to 3 uppercase letters (series, optional)
    - [0-9]{4}     : Ends with exactly 4 digits (registration number)
    - $            : End of string

    Accepts: Spaces, dashes (automatically removed)
    Example: DL01CA1234 or UP-16-Z-5555
    Usage: is_vehicle("DL01CA1234") -> True
    """
    clean_num = str(number).replace(" ", "").replace("-", "").upper()
    return bool(PATTERNS["vehicle"].match(clean_num))


def is_upi(upi_id: str) -> bool:
    """
    Validates UPI ID format.

    Regex: ^[\\w\\.\\-]+@[\\w\\.\\-]+$
    - ^[\\w\\.\\-]+ : Starts with word chars (a-z, A-Z, 0-9, _), dots, or dashes
    - @            : Literal '@' symbol (required)
    - [\\w\\.\\-]+  : Followed by word chars, dots, or dashes
    - $            : End of string

    Format: username@bankcode
    Example: user@paytm or john.doe@ybl
    Usage: is_upi("user@paytm") -> True
    """
    return bool(PATTERNS["upi"].match(str(upi_id)))


def is_gstin(gstin: str) -> bool:
    """
    Validates GSTIN with Modulo-36 checksum.

    Regex: ^\\d{2}[A-Z]{5}\\d{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$
    - ^\\d{2}       : Starts with 2 digits (state code)
    - [A-Z]{5}     : 5 uppercase letters (PAN first 5 chars)
    - \\d{4}       : 4 digits (sequential number)
    - [A-Z]{1}     : 1 letter (entity type)
    - [1-9A-Z]{1}  : 1 char: digit 1-9 or letter A-Z (sub-division)
    - Z            : Literal 'Z' (fixed char)
    - [0-9A-Z]{1}  : Check digit (alphanumeric)
    - $            : End of string

    Format: 2 digits + 5 letters + 4 digits + 1 letter + 1 alnum + Z + 1 alnum
    Checksum: Modulo-36 algorithm applied on first 14 characters
    Example: 27AAPFU0939F1ZV
    Usage: is_gstin("27AAPFU0939F1ZV") -> True
    """
    gstin = str(gstin).upper().strip()
    if not re.match(r"^\d{2}[A-Z]{5}\d{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$", gstin):
        return False

    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total = 0
    factor = 1

    try:
        for i in range(14):
            code_point = chars.index(gstin[i])
            product = factor * code_point
            digit = (product // 36) + (product % 36)
            total += digit
            factor = 2 if factor == 1 else 1

        check_code = (36 - (total % 36)) % 36
        return gstin[14] == chars[check_code]
    except ValueError:
        return False


def is_aadhaar(aadhaar: str) -> bool:
    """
    Validates Aadhaar number with Verhoeff checksum.

    Regex: ^[2-9]\\d{11}$
    - ^[2-9]       : Starts with digit 2-9 (cannot start with 0 or 1)
    - \\d{11}      : Followed by exactly 11 digits (0-9)
    - $            : End of string

    Total: 12 digits
    Checksum: Verhoeff algorithm on all 12 digits
    Accepts: Spaces, dashes (automatically removed)
    Example: 234123451234 or 2341-2345-1234
    Usage: is_aadhaar("234123451234") -> True
    """
    if not aadhaar:
        return False
    clean_num = str(aadhaar).replace(" ", "").replace("-", "")
    if not re.match(r"^[2-9]\d{11}$", clean_num):
        return False
    return validate_verhoeff(clean_num)


def is_voterid(voter_id: str) -> bool:
    """
    Validates Voter ID (EPIC) number.

    Regex: ^[A-Z]{3}[0-9]{7}$
    - ^[A-Z]{3}    : Starts with exactly 3 uppercase letters (state/region code)
    - [0-9]{7}     : Followed by exactly 7 digits (serial number)
    - $            : End of string

    Format: 3 letters + 7 digits (10 chars total)
    Example: ABC1234567 or XYZ9876543
    Usage: is_voterid("ABC1234567") -> True
    """
    if not voter_id:
        return False
    clean_id = str(voter_id).replace(" ", "").upper()
    return bool(PATTERNS["voterid"].match(clean_id))


def is_passport(passport: str) -> bool:
    """
    Validates Passport number.

    Regex: ^[A-Z][0-9]{7}$
    - ^[A-Z]       : Starts with exactly 1 uppercase letter (passport book type)
    - [0-9]{7}     : Followed by exactly 7 digits (serial number)
    - $            : End of string

    Format: 1 letter + 7 digits (8 chars total)
    Example: A1234567 or Z9876543
    Usage: is_passport("A1234567") -> True
    """
    if not passport:
        return False
    clean_pass = str(passport).replace(" ", "").upper()
    return bool(PATTERNS["passport"].match(clean_pass))


def is_cin(cin: str) -> bool:
    """
    Validates Corporate Identity Number (CIN).

    Regex: ^[LU]\\d{5}[A-Z]{2}\\d{4}[A-Z]{3}\\d{6}$
    - ^[LU]        : Starts with L (Limited) or U (Unlimited company)
    - \\d{5}       : 5 digits (industry classification code)
    - [A-Z]{2}     : 2 uppercase letters (state code)
    - \\d{4}       : 4 digits (year of incorporation)
    - [A-Z]{3}     : 3 uppercase letters (ownership code: PTC, PLC, OPC, GOI, etc.)
    - \\d{6}       : 6 digits (registration number)
    - $            : End of string

    Format: L/U + 5 digits + 2 letters + 4 digits + 3 letters + 6 digits (21 chars)
    Example: U12345MH2024PTC123456
    Usage: is_cin("U12345MH2024PTC123456") -> True
    """
    if not cin:
        return False
    cin = str(cin).replace(" ", "").upper()
    if len(cin) != 21:
        return False
    return bool(PATTERNS["cin"].match(cin))


def is_pincode(pincode: str) -> bool:
    """
    Validates Indian postal pincode.

    Regex: ^[1-9]\\d{5}$
    - ^[1-9]       : Starts with digit 1-9 (cannot start with 0)
    - \\d{5}       : Followed by exactly 5 digits (0-9)
    - $            : End of string

    Total: 6 digits, no leading zero
    Range: 100000 to 999999
    Example: 110001 or 560034
    Usage: is_pincode("110001") -> True
    """
    if not pincode:
        return False
    pincode = str(pincode).replace(" ", "")
    return bool(PATTERNS["pincode"].match(pincode))


def is_credit_card(card_number: str) -> bool:
    """
    Validates Credit/Debit Card numbers (Visa, MasterCard, RuPay, Amex).

    Uses the Luhn Algorithm (Mod 10) to verify the checksum digit.
    Accepts spaces and dashes (automatically removed).

    Example: 4532123456781234
    Usage: is_credit_card("4532 1234 5678 1234") -> True
    """
    if not card_number:
        return False

    clean_num = str(card_number).replace(" ", "").replace("-", "")

    if not PATTERNS["credit_card"].match(clean_num):
        return False

    return validate_luhn(clean_num)
