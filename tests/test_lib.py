import pytest
from indpy import (
    is_pan,
    is_tan,
    is_dl,
    is_gstin,
    is_vehicle,
    is_aadhaar,
    is_voterid,
    is_passport,
    is_mobile,
    is_ifsc,
    is_upi,
    is_cin,
    is_pincode,
    is_credit_card,
    Generate,
)


class TestPAN:
    def test_valid_pan(self):
        assert is_pan("ABCDE1234F") is True
        assert is_pan("CVZPC7403E") is True

    def test_invalid_pan(self):
        assert is_pan("ABCDE123") is False
        assert is_pan("12345ABCDE") is False
        assert is_pan("") is False
        assert is_pan("ABCDE1234F!") is False

    def test_pan_generator(self):
        generated = Generate.pan()
        assert is_pan(generated) is True
        assert len(generated) == 10


class TestTAN:
    def test_valid_tan(self):
        assert is_tan("DELM12345L") is True
        assert is_tan("ABCD12345Z") is True

    def test_invalid_tan(self):
        assert is_tan("DEL12345L") is False
        assert is_tan("DELM1234L") is False
        assert is_tan("DELM123456") is False
        assert is_tan("") is False

    def test_tan_generator(self):
        generated = Generate.tan()
        assert is_tan(generated) is True
        assert len(generated) == 10


class TestDL:
    def test_valid_dl(self):
        assert is_dl("MH1220140001234") is True
        assert is_dl("DL0120201234567") is True

    def test_valid_dl_with_separators(self):
        assert is_dl("MH12-2014-0001234") is True
        assert is_dl("MH12 2014 0001234") is True

    def test_invalid_dl(self):
        assert is_dl("MH122014000123") is False
        assert is_dl("M1220140001234") is False
        assert is_dl("") is False

    def test_dl_generator(self):
        generated = Generate.dl()
        assert is_dl(generated) is True
        assert len(generated) == 15


class TestGSTIN:
    def test_valid_gstin(self):
        assert is_gstin("27AAPFU0939F1ZV") is True

    def test_invalid_gstin_structure(self):
        assert is_gstin("27AAPFU0939F1Z") is False
        assert is_gstin("27AAPFU0939F1ZVX") is False

    def test_invalid_gstin_checksum(self):
        assert is_gstin("06AAACA6431N1ZA") is False

    def test_gstin_generator(self):
        generated = Generate.pan()
        assert len(generated) == 10


class TestAadhaar:
    def test_valid_aadhaar(self):
        assert is_aadhaar("787791992974") is True
        assert is_aadhaar("453842682677") is True

    def test_invalid_aadhaar_format(self):
        assert is_aadhaar("179980670385") is False
        assert is_aadhaar("37998067038") is False
        assert is_aadhaar("3799806703851") is False

    def test_invalid_aadhaar_checksum(self):
        assert is_aadhaar("379980670386") is False

    def test_aadhaar_generator(self):
        generated = Generate.aadhaar()
        assert is_aadhaar(generated) is True
        assert len(generated) == 12
        assert generated[0] in "23456789"


class TestVoterID:
    def test_valid_voterid(self):
        assert is_voterid("ABC1234567") is True
        assert is_voterid("XYZ9876543") is True

    def test_invalid_voterid_format(self):
        assert is_voterid("AB1234567") is False
        assert is_voterid("ABC123456") is False
        assert is_voterid("") is False

    def test_voterid_generator(self):
        generated = Generate.voterid()
        assert is_voterid(generated) is True
        assert len(generated) == 10
        assert generated[:3].isalpha() and generated[3:].isdigit()


class TestPassport:
    def test_valid_passport(self):
        assert is_passport("A1234567") is True
        assert is_passport("Z9876543") is True

    def test_invalid_passport_format(self):
        assert is_passport("12345678") is False
        assert is_passport("A123456") is False
        assert is_passport("A12345678") is False

    def test_passport_generator(self):
        generated = Generate.passport()
        assert is_passport(generated) is True
        assert len(generated) == 8
        assert generated[0].isalpha() and generated[1:].isdigit()


class TestMobile:
    def test_valid_mobile(self):
        assert is_mobile("9876543210") is True
        assert is_mobile("8765432109") is True
        assert is_mobile("7654321098") is True
        assert is_mobile("6543210987") is True

    def test_invalid_mobile_prefix(self):
        assert is_mobile("5432109876") is False
        assert is_mobile("4321098765") is False

    def test_invalid_mobile_format(self):
        assert is_mobile("987654321") is False
        assert is_mobile("98765432101") is False

    def test_mobile_generator(self):
        generated = Generate.mobile()
        assert is_mobile(generated) is True
        assert len(generated) == 10
        assert generated[0] in "6789"


class TestIFSC:
    def test_valid_ifsc(self):
        assert is_ifsc("SBIN0004321") is True
        assert is_ifsc("HDFC0000001") is True

    def test_invalid_ifsc_format(self):
        assert is_ifsc("SBIN000432") is False
        assert is_ifsc("SBIN00043210") is False
        assert is_ifsc("SBI00004321") is False

    def test_invalid_ifsc_fifth_char(self):
        assert is_ifsc("SBINA004321") is False


class TestVehicle:
    def test_valid_vehicle(self):
        assert is_vehicle("DL01CA1234") is True
        assert is_vehicle("UP16Z5555") is True
        assert is_vehicle("MH02AB1234") is True

    def test_invalid_vehicle_format(self):
        assert is_vehicle("DL01CA") is False
        assert is_vehicle("DL01CA12345") is False

    def test_vehicle_generator(self):
        generated = Generate.vehicle()
        assert is_vehicle(generated) is True
        assert len(generated) >= 9


class TestUPI:
    def test_valid_upi(self):
        assert is_upi("user@paytm") is True
        assert is_upi("john.doe@upi") is True
        assert is_upi("test-account_123@bank") is True

    def test_invalid_upi(self):
        assert is_upi("@paytm") is False
        assert is_upi("user@") is False
        assert is_upi("userpaytm") is False


class TestCIN:
    def test_valid_cin(self):
        assert is_cin("L99999MH2014PLC241895") is True

    def test_invalid_cin_format(self):
        assert is_cin("99999MH2014PLC241895") is False
        assert is_cin("L99999MH2014PLC24189") is False

    def test_invalid_cin_length(self):
        assert is_cin("L99999MH2014") is False
        assert is_cin("L99999MH2014PLC2418951") is False

    def test_cin_generator(self):
        generated = Generate.cin()
        assert is_cin(generated) is True
        assert len(generated) == 21


class TestPincode:
    def test_valid_pincode(self):
        assert is_pincode("560034") is True
        assert is_pincode("110001") is True
        assert is_pincode("400001") is True

    def test_invalid_pincode_leading_zero(self):
        assert is_pincode("012345") is False

    def test_invalid_pincode_format(self):
        assert is_pincode("56003") is False
        assert is_pincode("5600341") is False
        assert is_pincode("ABCDEF") is False

    def test_pincode_generator(self):
        generated = Generate.pincode()
        assert is_pincode(generated) is True
        assert len(generated) == 6
        assert generated[0] in "123456789"


class TestGeneratorConsistency:
    def test_generated_documents_validate(self):
        validators_and_generators = [
            (is_pan, Generate.pan),
            (is_tan, Generate.tan),
            (is_dl, Generate.dl),
            (is_aadhaar, Generate.aadhaar),
            (is_voterid, Generate.voterid),
            (is_passport, Generate.passport),
            (is_mobile, Generate.mobile),
            (is_vehicle, Generate.vehicle),
            (is_cin, Generate.cin),
            (is_pincode, Generate.pincode),
            (is_credit_card, Generate.credit_card),
        ]

        for validator, generator in validators_and_generators:
            for _ in range(10):
                generated = generator()
                assert (
                    validator(generated) is True
                ), f"Generated {generated} failed {validator.__name__} validation"


class TestEdgeCases:
    def test_empty_strings(self):
        assert is_pan("") is False
        assert is_gstin("") is False
        assert is_aadhaar("") is False
        assert is_voterid("") is False

    def test_whitespace(self):
        assert is_pan(" ABCDE1234F") is False
        assert is_aadhaar(" 787791992974") is True

    def test_special_characters(self):
        assert is_pan("ABCDE1234F!") is False
        assert is_aadhaar("379980670385@") is False

    def test_mixed_case(self):
        assert is_pan("abcde1234f") is True
        assert is_voterid("abc1234567") is True


class TestCreditCard:
    def test_valid_credit_card(self):
        assert is_credit_card("4111111111111111") is True
        assert is_credit_card("5555555555554444") is True
        assert is_credit_card("378282246310005") is True

    def test_valid_credit_card_with_separators(self):
        assert is_credit_card("4111 1111 1111 1111") is True
        assert is_credit_card("4111-1111-1111-1111") is True

    def test_invalid_credit_card(self):
        assert is_credit_card("4111111111111112") is False
        assert is_credit_card("123456789012") is False
        assert is_credit_card("") is False

    def test_credit_card_generator(self):
        generated = Generate.credit_card()
        assert is_credit_card(generated) is True
        assert len(generated) == 16
        assert generated[0] == "4"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
