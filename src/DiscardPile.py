class DiscardPile:
    def __init__(self):
        self.cards = []

    def add(self, card):
        if type(card) == list:
            self.cards += card
        else:
            self.cards.append(card)

    def remove(self, index):
        return self.cards.pop(index)

    def __str__(self):
        return str(list(map(str, self.cards)))
