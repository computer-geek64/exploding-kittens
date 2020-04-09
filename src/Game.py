from Deck import Deck
from Player import Player
from Card import Card
from random import randint


class Game:
    def __init__(self, players: list, imploding_kittens_expansion: bool = True, streaking_kittens_expansion: bool = True):
        self.players = [Player(x) for x in players]

        cards = Deck.original_deck
        if imploding_kittens_expansion:
            cards += Deck.imploding_kittens_expansion_deck
        if streaking_kittens_expansion:
            cards += Deck.streaking_kittens_expansion_deck

        self.deck = Deck(cards)
        self.deck.shuffle()

        c = 0
        for i in range(len(self.players)):
            self.players[i].hand.add(self.deck.draw_from_top())
            self.players[i].hand.add(self.deck.draw_from_top())
            self.players[i].hand.add(self.deck.draw_from_top())
            self.players[i].hand.add(self.deck.draw_from_top())
            self.players[i].hand.add(self.deck.draw_from_top())
            self.players[i].hand.add(self.deck.draw_from_top())
            self.players[i].hand.add(self.deck.draw_from_top())
            if c < len(Deck.defuse_cards):
                self.players[i].hand.add(Deck.defuse_cards[c])
                c += 1
            else:
                self.players[i].hand.add(Deck.defuse_cards[randint(0, len(Deck.defuse_cards) - 1)])

        if 2 <= len(self.players) <= 3:
            if c < len(Deck.defuse_cards):
                self.deck.insert_randomly(Deck.defuse_cards[c])
                c += 1
            else:
                self.deck.insert_randomly(Deck.defuse_cards[randint(0, len(Deck.defuse_cards) - 1)])

        i = 0
        for i in range(len(self.players) - 1):
            if i < len(Deck.exploding_kitten_cards):
                self.deck.insert_randomly(Deck.exploding_kitten_cards[i])
            else:
                self.deck.insert_randomly(Deck.exploding_kitten_cards[randint(0, len(Deck.exploding_kitten_cards) - 1)])

        if imploding_kittens_expansion:
            self.deck.insert_randomly(Card('imploding kitten', ''))
        elif streaking_kittens_expansion:
            if i < len(Deck.exploding_kitten_cards):
                self.deck.insert_randomly(Deck.exploding_kitten_cards[i])
            else:
                self.deck.insert_randomly(Deck.exploding_kitten_cards[randint(0, len(Deck.exploding_kitten_cards) - 1)])

        self.deck.shuffle()
