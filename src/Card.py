class Card:
    def __init__(self, action, id):
        self.action = action.lower()
        self.id = id.lower()
        self.image = self.action + ' ' + self.id + '.jpg'
        self.flipped = False

    def __str__(self):
        return self.action
