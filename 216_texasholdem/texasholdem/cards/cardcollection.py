from cards.card import Card, InvalidCardException


class CardCollection(object):

    '''The cards in a CardCollection are arranged in any order.'''

    def __init__(self):
        self._cards = []

    def add_card(self, card):
        if type(card) is not Card:
            raise InvalidCardException((
                'The first argument to the CardCollection.add_card'
                'method must be an instance of the Card class.'))
        self._cards.append(card)

    def count(self):
        return len(self._cards)

    def is_empty(self):
        return self.count == 0

    def __str__(self):
        result = ''
        for card in self._cards:
            result += str(card) + ' '

        return result.rstrip()
