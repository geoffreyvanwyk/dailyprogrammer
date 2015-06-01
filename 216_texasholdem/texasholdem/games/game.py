from .community import Community
from cards.deck import Deck
from .player import Player


class Game(object):

    CARDS_PER_PLAYER = 2

    def __init__(self, player_count):
        self._initialize_players(player_count)
        self.deck = Deck()
        self.community = Community()

    def _initialize_players(self, player_count):
        self.players = []
        for i in range(0, int(player_count)):
            self.players.append(Player())

    def deal_to_players(self):
        for i in range(0, Game.CARDS_PER_PLAYER):
            for player in self.players:
                player.hand.add_card(self.deck.draw())

    def deal_to_flop(self):
        for i in range(0, Community.CARDS_PER_FLOP):
            self.community.flop.add_card(self.deck.draw())

    def deal_to_turn(self):
        card = self.deck.draw()
        self.community.turn.suite = card.suite
        self.community.turn.number = card.number

    def deal_to_river(self):
        card = self.deck.draw()
        self.community.river.suite = card.suite
        self.community.river.number = card.number
