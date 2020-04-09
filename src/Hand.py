from Card import Card


class Hand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def play(self, index):
        return self.cards.pop(index)
