from ex1 import vat

def test_vat():
    assert vat( 10.00, False, "miscellaneous") == 12.00
