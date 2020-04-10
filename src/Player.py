from Hand import Hand


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = Hand()
        self.alive = True

    def __str__(self):
        return self.name
