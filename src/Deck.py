import Card
from random import randint


class Deck:
    original_deck = [
        Card('attack', 'back hair'),
        Card('attack', 'bear-o-dactyl'),
        Card('attack', 'catterwocky'),
        Card('attack', 'crab-a-pult'),
        Card('cat', 'bearded'),
        Card('cat', 'bearded'),
        Card('cat', 'bearded'),
        Card('cat', 'bearded'),
        Card('cat', 'catermelon'),
        Card('cat', 'catermelon'),
        Card('cat', 'catermelon'),
        Card('cat', 'catermelon'),
        Card('cat', 'hairy potato'),
        Card('cat', 'hairy potato'),
        Card('cat', 'hairy potato'),
        Card('cat', 'hairy potato'),
        Card('cat', 'rainbow-ralphing'),
        Card('cat', 'rainbow-ralphing'),
        Card('cat', 'rainbow-ralphing'),
        Card('cat', 'rainbow-ralphing'),
        Card('cat', 'tacocat'),
        Card('cat', 'tacocat'),
        Card('cat', 'tacocat'),
        Card('cat', 'tacocat'),
        Card('favor', 'back hair shampoo'),
        Card('favor', 'beard-sailing'),
        Card('favor', 'party squirrels'),
        Card('favor', 'peanut butter belly button'),
        Card('nope', 'jackanope'),
        Card('nope', 'ninja'),
        Card('nope', 'nopebell'),
        Card('nope', 'nopestradamus'),
        Card('nope', 'sandwich'),
        Card('see the future', 'all-seeing goat'),
        Card('see the future', 'mantis shrimp'),
        Card('see the future', 'pig-a-corn'),
        Card('see the future', 'special-ops bunnies'),
        Card('see the future', 'unicorn enchilada'),
        Card('shuffle', 'abracrab'),
        Card('shuffle', 'bat farts'),
        Card('shuffle', 'pomeranian storm'),
        Card('shuffle', 'transdimensional litter box'),
        Card('skip', 'bunnyraptor'),
        Card('skip', 'cheetah butt'),
        Card('skip', 'crab walk'),
        Card('skip', 'hypergoat')
    ]
    imploding_kittens_expansion_deck = []
    streaking_kittens_expansion_deck = []

    def __init__(self, players: int, imploding_kittens_expansion: bool, streaking_kittens_expansion: bool):
        if streaking_kittens_expansion and imploding_kittens_expansion:
            pass
        elif imploding_kittens_expansion:
            pass
        elif streaking_kittens_expansion:
            pass
        else:
            pass
        self.cards = []

    def draw(self, index):
        return self.cards.pop(index) if 0 <= index < len(self.cards) else None

    def draw_from_top(self):
        return self.draw(0)

    def draw_from_bottom(self):
        return self.draw(len(self.cards) - 1)

    def insert(self, index, card):
        self.cards.insert(index, card)