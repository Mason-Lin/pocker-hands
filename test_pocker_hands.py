import pocker_hands


def test_pocker_hands_compare():
    input = "Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH"
    assert pocker_hands.compare(input) == "White wins. - with high card: Ace"
