from cards.cardcollection import CardCollection
from cards.card import Card


class Community(object):

    CARDS_PER_FLOP = 3

    def __init__(self):
        self.flop = CardCollection()
        self.turn = Card()
        self.river = Card()
