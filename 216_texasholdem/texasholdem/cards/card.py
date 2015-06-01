import re


class Card(object):

    SUITES = ('♥', '♦', '♠ ', '♣')
    NUMBERS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self, suite=None, number=None):
        if suite is None and number is None:
            self._suite = None
            self._number = None
            return

        self.suite = suite
        self.number = number

    @property
    def suite(self):
        return self._suite

    @suite.setter
    def suite(self, suite):
        if suite not in Card.SUITES:
            raise InvalidCardException('The suite must be either' + re.sub(r"\(|\)|'", '', str(Card.SUITES)) + '.')
        self._suite = suite

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if number not in Card.NUMBERS:
            raise InvalidCardException(
                'The card number must be either ' + re.sub(r"\(|\)|'", '', str(Card.NUMBERS)) + '.'
            )
        self._number = number

    def __str__(self):
        return self.number + self.suite


class InvalidCardException(TypeError):
    pass
