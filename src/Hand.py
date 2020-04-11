from Card import Card


class Hand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def remove(self, index):
        return self.cards.pop(index)

    def flip(self, index):
        return self.cards[index]

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return str(list(map(str, self.cards)))
