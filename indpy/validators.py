"""
Core validation logic for Indian Identity and Financial documents.
Author: Harsh Gupta
License: MIT
"""

import re

# Pre-compiling regex patterns for performance efficiency
# Source: UIDAI and Income Tax Dept standards
PATTERNS = {
    "pan": re.compile(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"),
    "mobile": re.compile(r"^[6-9]\d{9}$"),
    "aadhaar_simple": re.compile(r"^[2-9]\d{11}$"),
    "ifsc": re.compile(r"^[A-Z]{4}0[A-Z0-9]{6}$"),
    "vehicle": re.compile(r"^[A-Z]{2}[0-9]{1,2}[A-Z]{0,3}[0-9]{4}$"),
    "upi": re.compile(r"^[\w\.\-]+@[\w\.\-]+$")
}

def is_pan(pan_number: str) -> bool:
    """
    Validates Permanent Account Number (PAN).
    Note: Currently implements Regex check. Checksum implementation pending v1.1.
    """
    if not isinstance(pan_number, str):
        return False
    return bool(PATTERNS["pan"].match(pan_number.upper()))

def is_mobile(number: str) -> bool:
    """
    Validates 10-digit Indian Mobile Numbers.
    Ignores +91 prefix if present.
    """
    if not number:
        return False
    
    # Sanitize input: remove spaces, dashes, +91
    clean_num = str(number).replace(" ", "").replace("-", "").replace("+91", "")
    return bool(PATTERNS["mobile"].match(clean_num))

def is_ifsc(code: str) -> bool:
    """
    Validates Indian Financial System Code (IFSC).
    Structure: 4 chars (Bank) + 0 + 6 chars (Branch).
    """
    return bool(PATTERNS["ifsc"].match(str(code).upper()))

def is_vehicle(number: str) -> bool:
    """
    Validates RC (Registration Certificate) Number.
    Example: DL01CA1234
    """
    clean_num = str(number).replace(" ", "").replace("-", "").upper()
    return bool(PATTERNS["vehicle"].match(clean_num))

def is_upi(upi_id: str) -> bool:
    """Validates UPI ID format (e.g., user@bank)."""
    return bool(PATTERNS["upi"].match(str(upi_id)))

def is_gstin(gstin: str) -> bool:
    """
    Validates Goods and Services Tax ID (GSTIN) with Checksum.
    Implements Modulo-36 hashing algorithm.
    """
    gstin = str(gstin).upper().strip()
    
    # 1. Format check
    regex_check = re.match(r"^\d{2}[A-Z]{5}\d{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$", gstin)
    if not regex_check:
        return False

    # 2. Checksum Logic (Modulo 36)
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total = 0
    factor = 1 

    try:
        for i in range(14):
            code_point = chars.index(gstin[i])
            product = factor * code_point
            
            # Sum the quotient and remainder
            digit = (product // 36) + (product % 36)
            total += digit
            
            # Toggle factor between 1 and 2
            factor = 2 if factor == 1 else 1
            
        check_code = (36 - (total % 36)) % 36
        return gstin[14] == chars[check_code]
        
    except ValueError:
        return False

def is_aadhaar(aadhaar: str) -> bool:
    """
    Validates Aadhaar format (12 digits).
    Rule: Cannot start with 0 or 1.
    """
    if not aadhaar:
        return False
    clean_num = str(aadhaar).replace(" ", "").replace("-", "")
    pattern = r"^[2-9]\d{11}$"    
    
    return bool(re.match(pattern, clean_num))
