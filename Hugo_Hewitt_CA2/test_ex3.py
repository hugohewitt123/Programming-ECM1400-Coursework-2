from ex3 import five_a_side_selector

def test_five_a_side_selector():
    names = ["David", "Ronaldo", "Matthew", "Jacq", "Johan", "Achim"]
    expected_result = [ ["David","Matthew","Johan"] , ["Ronaldo","Jacq","Achim"] ]
    assert five_a_side_selector(names) == expected_result
