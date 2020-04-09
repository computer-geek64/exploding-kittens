class Card:
    def __init__(self, action, id):
        self.action = action.lower()
        self.id = id.lower()
        self.image = self.action + '_' + self.id + '_card'
