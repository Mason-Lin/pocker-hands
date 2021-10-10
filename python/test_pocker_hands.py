import pytest
from pocker_hands import PokerGame


def test_compare_highcard():
    game = PokerGame(
        player1="Black",
        cards1="2H 3D 5S 9C KD",
        player2="White",
        cards2="2C 3H 4S 8C AH",
    )
    assert game.result() == "White wins. - with high card: A"


def test_compare_highcard_10():
    game = PokerGame(
        player1="Black",
        cards1="2H 3D 5S 9C 10D",
        player2="White",
        cards2="2C 3H 4S 8C 9H",
    )
    assert game.result() == "Black wins. - with high card: 10"


def test_compare_fullhouse():
    game = PokerGame(
        player1="Black",
        cards1="2S 8S AS QS 3S",
        player2="White",
        cards2="2H 4S 4C 2D 4H",
    )
    assert game.result() == "Black wins. - with full house: 4 over 2"


################# test internal functions #########################


def test_hand_card_parser():
    game = PokerGame()
    assert game.hand_card_parser("2H 3D 5S 9C 10D") == [
        "2H",
        "3D",
        "5S",
        "9C",
        "10D",
    ]


def test_split_card_to_suit_and_number():
    game = PokerGame()
    output = game.split_card_to_suit_and_number("10D")
    assert output == {"suit": "D", "number": "10"}


def test_compare_number_size():
    game = PokerGame()
    output = game.compare_number_size("K", "2")
    assert output == 1

    output = game.compare_number_size("Q", "Q")
    assert output == 0

    output = game.compare_number_size("10", "A")
    assert output == -1
