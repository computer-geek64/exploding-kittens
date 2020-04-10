from Hand import Hand
from Card import Card


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = Hand()
        self.alive = True

    def show_hand(self):
        return [x if x.flipped else Card('hidden', '') for x in self.hand.cards]

    def __str__(self):
        return self.name
