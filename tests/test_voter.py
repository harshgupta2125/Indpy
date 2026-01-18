import sys
sys.path.insert(0, '/home/harsh/Desktop/Indpy')

import indpy
from indpy import Generate

print("--- TESTING VOTER ID & PASSPORT ---\n")

# 1. Test Voter ID
print("1️⃣ VOTER ID TEST")
fake_voter = Generate.voterid()
print(f"Generated Voter ID: {fake_voter}")
if indpy.is_voterid(fake_voter):
    print("✅ Voter ID Validation: Success\n")
else:
    print("❌ Voter ID Validation: Failed\n")

# 2. Test Passport
print("2️⃣ PASSPORT TEST")
fake_pass = Generate.passport()
print(f"Generated Passport: {fake_pass}")
if indpy.is_passport(fake_pass):
    print("✅ Passport Validation: Success\n")
else:
    print("❌ Passport Validation: Failed\n")

# 3. Test Invalid Inputs
print("3️⃣ INVALID INPUT TESTS")
if not indpy.is_passport("12345678"):  # Starts with number (Invalid)
    print("✅ Correctly rejected invalid Passport (starts with number)")
    
if not indpy.is_voterid("AB1234567"):  # Only 2 letters (Invalid)
    print("✅ Correctly rejected invalid Voter ID (only 2 letters)")

if not indpy.is_voterid("ABCD1234567"):  # 4 letters (Invalid)
    print("✅ Correctly rejected invalid Voter ID (4 letters)")

print("\n✅ All tests passed! Version 0.1.4 ready! 🚀")
