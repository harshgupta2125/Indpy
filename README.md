# indpy 🇮🇳

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/status-production-success?style=for-the-badge)
![PyPI](https://img.shields.io/badge/PyPI-0.1.4-blue?style=for-the-badge)

indpy is a comprehensive Python library for validating and generating Indian government documents and financial identifiers. It uses official checksum algorithms (GSTIN Mod-36, Aadhaar Verhoeff) where applicable and provides regex-based structural validation for all document types.

## 🚀 Features

### ✅ Validation (11 Document Types)
- **PAN**: Permanent Account Number (5 letters + 4 digits + 1 letter)
- **GSTIN**: GST Identification Number (with Mod-36 checksum verification)
- **Aadhaar**: 12-digit unique identity (with Verhoeff checksum algorithm)
- **Voter ID (EPIC)**: Electoral ID (3 letters + 7 digits)
- **Passport**: Passport number (1 letter + 7 digits)
- **Mobile**: Indian 10-digit format (starts with 6–9)
- **IFSC**: Bank branch code (4 letters + 0 + 6 alphanumeric)
- **Vehicle (RC)**: Registration certificate (state code + regional code + registration)
- **UPI**: Unified Payments Interface handle
- **CIN**: Corporate Identification Number (21-character corporate format)
- **Pincode**: Indian postal code (6 digits, no leading zero)

### 🎲 Data Generation (8 Mock Data Generators)
- Generate valid PAN numbers with realistic format
- Generate valid mobile numbers (6–9 prefix)
- Generate valid Aadhaar numbers with mathematically correct Verhoeff checksum
- Generate Voter ID numbers
- Generate Passport numbers
- Generate Vehicle registration numbers
- Generate CIN numbers
- Generate Pincode numbers

---

## 📦 Installation

Install from PyPI:

```bash
pip install indpy_core
```

Note: The package name on PyPI is `indpy_core`, but you import it in Python as `indpy`.

Install for local development:

```bash
# Clone the repository
git clone https://github.com/harshgupta2125/Indpy.git
cd Indpy
pip install -e .
```

## 💻 Usage

### 1️⃣ Python — Validation

```python
from indpy import (
    is_pan, is_gstin, is_vehicle, is_aadhaar, is_voterid, 
    is_passport, is_mobile, is_ifsc, is_upi, is_cin, is_pincode
)

# Validate PAN (Permanent Account Number)
print(is_pan("ABCDE1234F"))  # True

# Validate GSTIN (includes official Mod-36 checksum)
print(is_gstin("29ABCDE1234F1Z5"))  # True/False based on checksum

# Validate Aadhaar (12-digit with Verhoeff checksum algorithm)
print(is_aadhaar("379980670385"))  # True/False based on Verhoeff

# Validate Voter ID (EPIC format)
print(is_voterid("ABC1234567"))  # True

# Validate Passport
print(is_passport("A1234567"))  # True

# Validate Mobile number (Indian format, 6-9 prefix)
print(is_mobile("9876543210"))  # True

# Validate IFSC code (Bank branch)
print(is_ifsc("SBIN0004321"))  # True

# Validate Vehicle registration number
print(is_vehicle("DL01CA1234"))  # True

# Validate UPI handle
print(is_upi("user@paytm"))  # True

# Validate CIN (Corporate Identification Number)
print(is_cin("L99999MH2014PLC241895"))  # True

# Validate Pincode (6 digits, no leading zero)
print(is_pincode("560034"))  # True
```

### 2️⃣ Python — Generating Mock Data

```python
from indpy import Generate

# Generate random PAN
print(Generate.pan())      # e.g. "BPLPZ5821K"

# Generate random mobile number
print(Generate.mobile())   # e.g. "9876123450"

# Generate random Aadhaar (with mathematically valid Verhoeff checksum)
print(Generate.aadhaar())  # e.g. "379980670385"

# Generate random Voter ID
print(Generate.voterid())  # e.g. "ABC1234567"

# Generate random Passport
print(Generate.passport()) # e.g. "A1234567"

# Generate random Vehicle registration
print(Generate.vehicle())  # e.g. "DL04CA9921"

# Generate random CIN
print(Generate.cin())      # e.g. "L12345AB2024PLC123456"

# Generate random Pincode
print(Generate.pincode())  # e.g. "560034"
```

### 3️⃣ Command Line Interface

Check version:

```bash
indpy --version
# Output: 0.1.4
```

Validate a document:

```bash
# Validate PAN
indpy check pan ABCDE1234F
# Output: ✅ PAN Validation Result: True

# Validate Aadhaar
indpy check aadhaar 379980670385
# Output: ✅ AADHAAR Validation Result: True

# Validate Voter ID
indpy check voterid ABC1234567
# Output: ✅ VOTERID Validation Result: True

# Validate Passport
indpy check passport A1234567
# Output: ✅ PASSPORT Validation Result: True

# Validate CIN
indpy check cin L99999MH2014PLC241895
# Output: ✅ CIN Validation Result: True

# Validate Pincode
indpy check pincode 560034
# Output: ✅ PINCODE Validation Result: True
```

Generate mock data:

```bash
# Generate PAN
indpy gen pan
# Output: ABCDE1234F

# Generate Aadhaar
indpy gen aadhaar
# Output: 379980670385

# Generate Vehicle
indpy gen vehicle
# Output: DL04CA9921

# Generate Voter ID
indpy gen voterid
# Output: ABC1234567

# Generate Passport
indpy gen passport
# Output: A1234567

# Generate CIN
indpy gen cin
# Output: L12345AB2024PLC123456

# Generate Pincode
indpy gen pincode
# Output: 560034
```

## 🛠️ Supported Documents

| Document | Regex Pattern | Checksum | Notes |
|:---------|:--------------|:--------:|:------|
| PAN | `^[A-Z]{5}[0-9]{4}[A-Z]$` | Structure only | 10-character format |
| GSTIN | `^[0-9]{2}[A-Z]{5}[0-9A-Z]{9}[0-9]$` | **Mod-36** | 15-character GST ID |
| Aadhaar | `^[2-9]\d{11}$` | **Verhoeff** | 12-digit unique ID |
| Voter ID | `^[A-Z]{3}[0-9]{7}$` | N/A | EPIC format |
| Passport | `^[A-Z][0-9]{7}$` | N/A | 8-character format |
| Mobile | `^[6-9]\d{9}$` | N/A | 10-digit Indian number |
| IFSC | `^[A-Z]{4}0[A-Z0-9]{6}$` | N/A | Bank branch code |
| Vehicle | `^[A-Z]{2}\d{1,2}[A-Z]{1,2}\d{1,4}$` | N/A | State code + registration |
| UPI | `^[a-zA-Z0-9.\-_]+@[a-zA-Z]+$` | N/A | Payment handle |
| CIN | `^[A-Z][0-9]{5}[A-Z]{2}[0-9]{4}[A-Z]{3}[0-9]{6}$` | N/A | Corporate ID (21-char) |
| Pincode | `^[1-9]\d{5}$` | N/A | 6-digit postal code |
� Testing

Run the comprehensive test suite:

```bash
# Run all tests
python3 -m pytest tests/

# Run specific test file
python3 -m pytest tests/test_lib.py -v

# Run with coverage
python3 -m pytest tests/ --cov=indpy
```

Test files include:
- **test_lib.py**: Comprehensive tests for all 11 validators and 8 generators
- Coverage includes structural validation, checksum algorithms, and edge cases

## 🤝 Contributing

Contributions are welcome! Typical workflow:

1. Fork the repository
2. Create a feature branch:
   ```bash
   git checkout -b feature/NewValidator
   ```
3. Add your validator to [indpy/validators.py](indpy/validators.py)
4. Add corresponding generator to [indpy/generators.py](indpy/generators.py)
5. Update [indpy/__init__.py](indpy/__init__.py) to export new functions
6. Add tests to [tests/test_lib.py](tests/test_lib.py)
7. Commit with clear message:
   ```bash
   git commit -m "Add new validator for [document type]"
   ```
8. Push and open a pull request

**Code Style:**
- Follow PEP 8 standards
- Add comprehensive docstrings with regex patterns
- Include usage examples in docstrings
- Test coverage for all new validators

## 📚 API Reference

All validators return a **boolean** (True/False). All generators return a **string**.

### Validators
```python
is_pan(pan: str) -> bool
is_gstin(gstin: str) -> bool
is_aadhaar(aadhaar: str) -> bool
is_voterid(voterid: str) -> bool
is_passport(passport: str) -> bool
is_mobile(mobile: str) -> bool
is_ifsc(ifsc: str) -> bool
is_vehicle(vehicle: str) -> bool
is_upi(upi: str) -> bool
is_cin(cin: str) -> bool
is_pincode(pincode: str) -> bool
```

### Generators
```python
Generate.pan() -> str
Generate.gstin() -> str  # Note: Does not generate checksum
Generate.aadhaar() -> str  # With valid Verhoeff checksum
Generate.voterid() -> str
Generate.passport() -> str
Generate.mobile() -> str
Generate.vehicle() -> str
Generate.cin() -> str
Generate.pincode() -> str
```

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

## 📊 Project Status

**Version:** 0.1.5

**Features:**
- ✅ 11 document validators (all functional)
- ✅ 8 mock data generators (production-ready)
- ✅ Official checksum algorithms (Verhoeff, Mod-36)
- ✅ Comprehensive documentation with regex patterns
- ✅ CLI support for validation and generation
- ✅ PEP 8 compliant codebase
- ✅ Full test coverage

**Roadmap:**
- [ ] Add Driving License validator
- [ ] Add Enrollment ID (UID) validator
- [ ] Add GST Certificate validator
- [ ] Add international passport format support
```bash
git add README.md
git commit -m "Update README formatting"
git push origin main
```
