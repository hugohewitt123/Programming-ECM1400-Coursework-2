from ex2 import email_addresses

def test_email_addresses():
    first = ["David", "Matthew"]
    last = ["Wakeling", "Collison"]
    expected_result = [ "d.wakeling@exeter.ac.uk", "m.collison@exeter.ac.uk" ]
    assert email_addresses(first, last) == expected_result
