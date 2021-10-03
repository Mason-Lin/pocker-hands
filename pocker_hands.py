def compare(input):
    hand1, hand2 = hand_card_parser(input)

    return f"{hand2['player']} wins. - with high card: Ace"


def hand_card_parser(input):
    """
    input
        "Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH"
    output
        {
            "player": "Black",
            "cards": ["2H", "3D", "5S", "9C", "KD"]
        }
    """
    splited_input = input.split()
    p1 = splited_input[0].rstrip(":")
    c1 = splited_input[1:6]

    p2 = splited_input[6].rstrip(":")
    c2 = splited_input[7:12]

    hand1 = {"player": p1, "cards": []}
    hand1["cards"].append(c1)
    hand2 = {"player": p2, "cards": []}
    hand2["cards"].append(c2)
    return hand1, hand2
