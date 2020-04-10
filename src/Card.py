class Card:
    def __init__(self, action, id):
        self.action = action.lower()
        self.id = id.lower()
        self.image = self.action + ' ' + self.id + '.png'

    def __str__(self):
        return '<Card: ' + self.action + ', id: ' + self.id + '>'
