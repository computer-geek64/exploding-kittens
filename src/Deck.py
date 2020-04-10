from Card import Card
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
    exploding_kitten_cards = [
        Card('exploding kitten', 'earth'),
        Card('exploding kitten', 'ship'),
        Card('exploding kitten', 'boat'),
        Card('exploding kitten', 'house')
    ]
    defuse_cards = [
        Card('defuse', 'laser pointer'),
        Card('defuse', 'therapy'),
        Card('defuse', 'belly rub'),
        Card('defuse', 'catnip sandwich'),
        Card('defuse', 'yoga'),
        Card('defuse', '3am flatulence')
    ]

    def __init__(self, cards: list):
        self.cards = cards

    def draw(self, index):
        return self.cards.pop(index) if 0 <= index < len(self.cards) else None

    def draw_from_top(self):
        return self.draw(0)

    def draw_from_bottom(self):
        return self.draw(len(self.cards) - 1)

    def insert(self, index, card):
        self.cards.insert(index, card)

    def insert_randomly(self, card):
        self.cards.insert(randint(0, len(self.cards)), card)

    def shuffle(self):
        temp = self.cards
        self.cards = []
        while len(temp) > 0:
            self.cards.append(temp.pop(randint(0, len(temp) - 1)))

    def __str__(self):
        return str(list(map(str, self.cards)))
