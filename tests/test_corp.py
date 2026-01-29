import indpy
from indpy import Generate

# Test CIN
fake_cin = Generate.cin()
print(f"Generated CIN: {fake_cin}")
if indpy.is_cin(fake_cin):
    print("✅ CIN Valid")
else:
    print("❌ CIN Invalid")

# Test Pincode
fake_pin = Generate.pincode()
print(f"Generated Pin: {fake_pin}")
if indpy.is_pincode(fake_pin):
    print("✅ Pincode Valid")

# Test Invalid Pincode
if not indpy.is_pincode("203131"):  # Starts with 0
    print("✅ Correctly rejected invalid pincode")
