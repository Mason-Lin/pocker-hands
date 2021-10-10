class PokerGame:
    def __init__(self, player1=None, cards1=None, player2=None, cards2=None):
        self.player1 = player1
        if cards1 is not None:
            self.cards1 = [
                self.split_card_to_suit_and_number(card)
                for card in self.hand_card_parser(cards1)
            ]
        self.player2 = player2
        if cards2 is not None:
            self.cards2 = [
                self.split_card_to_suit_and_number(card)
                for card in self.hand_card_parser(cards2)
            ]

    def hand_card_parser(self, input):
        """
        input
            "2H 3D 5S 9C KD"
        output
            ["2H", "3D", "5S", "9C", "KD"]
        """
        splited_input = input.split()
        return splited_input

    def split_card_to_suit_and_number(self, card):
        new_card = {"suit": card[-1], "number": card[:-1]}
        return new_card

    def compare_number_size(self, number1, number2):
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
        size1 = mapping_order.index(number1)
        size2 = mapping_order.index(number2)
        if size1 > size2:
            return 1
        elif size1 == size2:
            return 0
        else:
            return -1

    def get_biggest_card(self, cards):
        biggest = cards[0]["number"]
        for card in cards:
            if self.compare_number_size(card["number"], biggest) == 1:
                biggest = card["number"]
        return biggest

    def is_full_house(self, cards):
        suits = [card["suit"] for card in cards]
        return len(set(suits)) == 1

    def get_full_house_details(self, cards):
        numbers = sorted([card["number"] for card in cards])
        triple = numbers[2]
        double = numbers[-1] if numbers[2] == numbers[0] else numbers[0]
        return triple, double

    def result(self):
        winner = "No one"
        reasons = "same card"
        big1 = self.get_biggest_card(self.cards1)
        big2 = self.get_biggest_card(self.cards2)
        if self.compare_number_size(big1, big2) == 1:
            winner = self.player1
            reasons = f"high card: {big1}"
        elif self.compare_number_size(big1, big2) == -1:
            winner = self.player2
            reasons = f"high card: {big2}"
        else:
            pass

        if self.is_full_house(self.cards1) and self.is_full_house(self.cards2):
            triple1, double1 = self.get_full_house_details(self.cards1)
            triple2, double2 = self.get_full_house_details(self.cards2)
            if triple1 > triple2:
                winner = self.player1
                reasons = f"full house: {triple1} over {double1}"
            elif triple1 < triple2:
                winner = self.player2
                reasons = f"full house: {triple2} over {double2}"
            else:
                if double1 > double2:
                    winner = self.player1
                    reasons = f"full house: {triple1} over {double1}"
                elif double1 < double2:
                    winner = self.player2
                    reasons = f"full house: {triple2} over {double2}"
                else:
                    pass
        elif self.is_full_house(self.cards1):
            winner = self.player1
            triple, double = self.get_full_house_details(self.cards1)
            reasons = f"full house: {triple} over {double}"
        elif self.is_full_house(self.cards2):
            winner = self.player2
            triple, double = self.get_full_house_details(self.cards2)
            reasons = f"full house: {triple} over {double}"
        else:
            pass

        result_message = f"{winner} wins. - with {reasons}"
        return result_message
