# indpy 🇮🇳

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/status-stable-success?style=for-the-badge)

indpy is a Python library for validating and generating Indian government documents and financial identifiers. It implements official checksum algorithms (where applicable) to ensure data integrity.

## 🚀 Features

### ✅ Validation
- PAN Card: structure validation.
- GSTIN: structure + Modulo-36 checksum verification.
- Mobile Number: Indian 10-digit format (starts with 6–9).
- IFSC Code: bank branch code validation.
- Vehicle (RC) Number: standard RTO formats (e.g., DL01CA1234).
- UPI ID: standard handle validation.

### 🎲 Data generation (mock data)
- Generate valid PAN numbers for testing.
- Generate valid mobile numbers.
- Generate random vehicle registration numbers.

---

## 📦 Installation

Install from PyPI:

```bash
pip install indpy
```

Install for local development:

```bash
git clone https://github.com/YOUR_USERNAME/indpy.git
cd indpy
pip install -e .
```

## 💻 Usage

### 1) Python — Validation

```python
from indpy import is_pan, is_gstin, is_vehicle

# Validate PAN
if is_pan("ABCDE1234F"):
    print("Valid PAN")

# Validate GSTIN (includes checksum)
if is_gstin("29ABCDE1234F1Z5"):
    print("Valid GSTIN")
else:
    print("Invalid GSTIN or checksum mismatch")

# Validate Vehicle registration
print(is_vehicle("UP16Z5555"))  # True or False
```

### 2) Python — Generating mock data

```python
from indpy import Generate

# Random PAN
print(Generate.pan())     # e.g. "BPLPZ5821K"

# Random Mobile
print(Generate.mobile())  # e.g. "9876123450"

# Random Vehicle
print(Generate.vehicle()) # e.g. "DL04CA9921"
```

### 3) Command line interface

Check version:

```bash
indpy --version
```

Validate a document:

```bash
indpy check pan ABCDE1234F
# Output: ✅ PAN Validation Result: True
```

Generate fake data:

```bash
indpy gen pan
# Output: ABCDE1234F

indpy gen vehicle
# Output: DL04CA9921
```

## 🛠️ Supported documents

| Document | Regex / Logic (approx.) | Checksum implemented? |
|---------:|-------------------------|:---------------------:|
| PAN | `[A-Z]{5}[0-9]{4}[A-Z]{1}` | ❌ (structure only; checksum planned v1.1) |
| GSTIN | `\d{2}[A-Z]{5}[0-9A-Z]{9}` (Modulo-36 checksum) | ✅ |
| Mobile | `[6-9]\d{9}` | N/A |
| IFSC | `[A-Z]{4}0[A-Z0-9]{6}` | N/A |
| Vehicle (RC) | `[A-Z]{2}\d{1,2}[A-Z]{1,2}\d{1,4}` (varies by state) | N/A |

> Note: Regex shown are illustrative and may be refined in code. GSTIN validation includes official Modulo-36 checksum verification.

## 🤝 Contributing

Contributions welcome. Typical workflow:

1. Fork the repository.
2. Create a feature branch: git checkout -b feature/NewValidation
3. Commit your changes: git commit -m "Add Aadhaar support"
4. Push and open a pull request.

Please follow the existing code style and include tests for new validations.

## 📄 License

Distributed under the MIT License. See LICENSE for details.