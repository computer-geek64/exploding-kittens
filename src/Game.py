from Deck import Deck
from DiscardPile import DiscardPile
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
        self.discard_pile = DiscardPile()
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
        self.turn_queue = list(map(str, self.players))

    def get_player_by_name(self, name):
        return [x for x in self.players if x.name == name][0]

    def remove_player(self, name):
        index = [i for i in range(len(self.deck.cards)) if self.deck.cards[i].action == 'exploding kitten']
        if len(index) > 0:
           self.discard_pile.add(self.deck.draw(index))
        self.discard_pile.add(self.get_player_by_name(name).hand.cards)
        self.turn_queue.remove(name)
        self.players.remove(self.get_player_by_name(name))

    def play_card(self, cards, player, target=None, target_card=None):
        for card in cards:
            self.get_player_by_name(player).hand.cards.remove(card)
        if len(cards) == 1:
            if cards[0].action == 'attack':
                self.turn_queue = list(dict.fromkeys(self.turn_queue))
                self.end_turn()
                self.turn_queue.insert(0, self.turn_queue[0])
            elif cards[0].action == 'targeted attack':
                self.turn_queue = list(dict.fromkeys(self.turn_queue))
                while not self.turn_queue[0] == target:
                    self.end_turn()
                self.turn_queue.insert(0, target)
            elif cards[0].action == 'favor':
                self.get_player_by_name(target).select_card = True
            elif cards[0].action == 'nope':
                pass
            elif cards[0].action == 'see the future':
                self.get_player_by_name(player).see_the_future.append(self.deck.draw_from_top())
                self.get_player_by_name(player).see_the_future.append(self.deck.draw_from_top())
                self.get_player_by_name(player).see_the_future.append(self.deck.draw_from_top())
        elif len(cards) == 2 and cards[0].action == cards[1].action:
            self.get_player_by_name(player).hand.add(self.get_player_by_name(target).pick_from_randomly())
        elif len(cards) == 3 and cards[0].action == cards[1].action and cards[1].action == cards[2].action:
            self.get_player_by_name(player).hand.add(self.get_player_by_name(target).pick_card(target_card))

    def end_turn(self):
        x = self.turn_queue.pop(0)
        if x not in self.turn_queue:
            self.turn_queue.append(x)
