from random import shuffle
from cards.card import Card
from cards.cardcollection import CardCollection


class Deck(CardCollection):

    '''The cards in a Deck is a stack data structure.'''

    def __init__(self):
        CardCollection.__init__(self)
        for suite in Card.SUITES:
            for number in Card.NUMBERS:
                self.add_card(Card(suite, number))

    def shuffle(self):
        shuffle(self._cards)

    def draw(self):
        if self.is_empty():
            raise EmptyDeckException('The deck is empty.')
        return self._cards.pop()


class EmptyDeckException(Exception):
    pass
