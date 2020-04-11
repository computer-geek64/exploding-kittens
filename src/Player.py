from Hand import Hand
from Card import Card
from random import randint


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = Hand()
        self.alive = True
        self.blind = False
        self.select_card = False
        self.see_the_future = []
        self.alter_the_future = []

    def show_hand(self):
        return [x if x.flipped else Card('card back', '') for x in self.hand.cards]

    def pick_from_randomly(self):
        return self.hand.remove(randint(0, len(self.hand) - 1))

    def pick_card(self, card):
        return self.hand.remove([i for i in range(len(self.hand.cards)) if self.hand.cards[i].action == card][0])

    def __str__(self):
        return self.name