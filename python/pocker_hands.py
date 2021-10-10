import enum


def split_to_suit_and_size(cards):
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
    new_cards = []
    for card in cards:
        new_card = {"suit": card[-1], "size": mapping_order.index(card[:-1])}
        new_cards.append(new_card)
    new_cards.sort(key=lambda x: x["size"])
    return new_cards


def compare(input):
    hand1, hand2 = hand_card_parser(input)
    hand1["cards"] = split_to_suit_and_size(hand1["cards"])
    hand2["cards"] = split_to_suit_and_size(hand2["cards"])

    biggest_h1 = hand1["cards"][-1]["size"]
    biggest_h2 = hand2["cards"][-1]["size"]

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

    hand1 = {"player": p1, "cards": c1}
    hand2 = {"player": p2, "cards": c2}
    return hand1, hand2
