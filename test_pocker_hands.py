import pytest
import pocker_hands


def test_pocker_hands_compare_highcard():
    input = "Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH"
    assert pocker_hands.compare(input) == "White wins. - with high card: Ace"


@pytest.mark.skip()
def test_pocker_hands_compare_fullhouse():
    input = "Black: 2H 4S 4C 2D 4H  White: 2S 8S AS QS 3S"
    assert (
        pocker_hands.compare(input) == "Black wins. - with full house: 4 over 2"
    )
