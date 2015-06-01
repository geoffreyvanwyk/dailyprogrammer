from cards.cardcollection import CardCollection


class Player(object):

    def __init__(self):
        self.hand = CardCollection()
