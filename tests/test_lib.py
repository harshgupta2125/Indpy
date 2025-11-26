# Look! We are importing it just like a standard library
import indpy

print("--- TESTING INDPY LIBRARY ---")

# 1. Test Mobile Number
# ---------------------
my_num = "9876543210"
if indpy.is_mobile(my_num):
    print(f"✅ Mobile '{my_num}' is VALID")
else:
    print(f"❌ Mobile '{my_num}' is INVALID")

# 2. Test PAN Card
# ----------------
my_pan = "CVZPC7403E"
if indpy.is_pan(my_pan):
    print(f"✅ PAN '{my_pan}' is VALID")
else:
    print(f"❌ PAN '{my_pan}' is INVALID")

# 3. Test GSTIN (The Complex Math Check)
# --------------------------------------
# This is a REAL valid GSTIN (Haryana Govt sample)
# A verified valid GSTIN (Flipkart's GSTIN)
real_gst = "27AAPFU0939F1ZV"# This is a FAKE GSTIN (I changed the last letter Q to A)
fake_gst = "06AAACA6431N1ZA"

print("\nChecking GST Checksum Logic:")

if indpy.is_gstin(real_gst):
    print(f"✅ Real GSTIN '{real_gst}' PASSED math check!")
else:
    print(f"❌ Real GSTIN failed (Logic Error)")

if indpy.is_gstin(fake_gst) == False:
    print(f"✅ Fake GSTIN '{fake_gst}' was caught correctly!")
else:
    print(f"❌ Fake GSTIN bypassed the check (Logic Error)")

# 4. Test Other Validators
# -------------------------
# Validation
if indpy.is_ifsc("SBIN0004321"):
    print("Bank Valid")

if indpy.is_vehicle("UP16Z5555"):
    print("Car Valid")

# Generation (The cool part)
dummy_pan = indpy.Generate.pan()
print(f"Generated Test PAN: {dummy_pan}")