def compare(input):
    hand1, hand2 = hand_card_parser(input)
    mapping_order = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
        "A",
    ]
    biggest_h1 = mapping_order.index(hand1["cards"][-1][0])
    biggest_h2 = mapping_order.index(hand2["cards"][-1][0])

    if biggest_h1 < biggest_h2:
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
    hand1["cards"].extend(c1)

    hand2 = {"player": p2, "cards": []}
    hand2["cards"].extend(c2)
    return hand1, hand2
