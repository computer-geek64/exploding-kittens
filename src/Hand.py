import Card


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def add(self, card):
        self.cards.append(card)

    def play(self, index):
        return self.cards.pop(index)
