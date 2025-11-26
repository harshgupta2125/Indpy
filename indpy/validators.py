import re

def is_mobile(number: str) -> bool:
    """
    Validates Indian Mobile Number.
    Accepts: '9876543210', '+919876543210', '+91 9876543210'
    """
    # Clean the number: Remove spaces, dashes, and +91
    clean_num = str(number).replace(" ", "").replace("-", "").replace("+91", "")
    
    # Check if it is exactly 10 digits and starts with 6, 7, 8, or 9
    pattern = r"^[6-9]\d{9}$"
    return bool(re.match(pattern, clean_num))

def is_pan(pan: str) -> bool:
    """
    Validates Indian PAN Card format.
    Format: 5 Letters, 4 Digits, 1 Letter (e.g., ABCDE1234F)
    """
    pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"
    return bool(re.match(pattern, pan.upper()))

def is_gstin(gstin: str) -> bool:
    """
    Validates GSTIN using Checksum Algorithm.
    Format: 22AAAAA0000A1Z5
    """
    gstin = gstin.upper().strip()
    
    # Step 1: Basic Regex Check (15 chars total)
    # 2 digits + 5 letters + 4 digits + 1 letter + 1 digit + 'Z' + 1 char
    if not re.match(r"^\d{2}[A-Z]{5}\d{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$", gstin):
        return False

    # Step 2: The Checksum Math (Modulo 36)
    # This ensures the number is mathematically valid
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    total = 0
    factor = 1 # We multiply by 1, then 2, then 1...

    # Loop through first 14 characters
    for i in range(14):
        code_point = chars.find(gstin[i]) # Get value (A=10, B=11...)
        
        product = factor * code_point
        
        # Add quotient and remainder to total
        digit = (product // 36) + (product % 36)
        total += digit
        
        # Toggle factor (if 1 make 2, if 2 make 1)
        factor = 2 if factor == 1 else 1
        
    # Calculate what the last digit SHOULD be
    check_val = (36 - (total % 36)) % 36
    calculated_char = chars[check_val]
    
    # Compare with actual last digit
    return gstin[14] == calculated_char