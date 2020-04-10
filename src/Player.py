from Hand import Hand


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = Hand()

    def __str__(self):
        return '<Player: ' + self.name + ', Hand: ' + str(self.hand) + '>'