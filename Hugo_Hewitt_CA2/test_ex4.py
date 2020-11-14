from ex4 import obfuscate

def test_obfuscate():
    input_text = "Hello the world"
    expected_result = "HeLlo boE wOrlD"
    assert obfuscate(input_text) == expected_result
