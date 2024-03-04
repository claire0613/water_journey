from Card import Card


class Hand:

    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card):
        if len(self.cards) >= 13:
            raise ValueError("The hand's size must not exceed 13.")
        self.cards.append(card)

    def get(self, index):
        return self.cards[index]

    def show(self, index):
        return self.cards.pop(index)

    def size(self):
        return len(self.cards)

