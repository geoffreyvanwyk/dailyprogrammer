from .game import Game


DISPLAY_WIDTH = 50
FILLER = '='
END = '#'


def main():
    print_title()

    player_count = get_player_count()

    game = Game(player_count)
    game.deck.shuffle()
    game.deal_to_players()
    game.deal_to_flop()
    game.deal_to_turn()
    game.deal_to_river()

    show_hands(game)


def show_hands(game):
    print()
    print_heading('hands')

    print('Yours: ' + str(game.players[0].hand))
    for i in range(1, len(game.players)):
        print('Player' + str(i) + ': ' + str(game.players[i].hand))

    print()
    print_heading('community')

    print('Flop: ' + str(game.community.flop))
    print('Turn: ' + str(game.community.turn))
    print('River: ' + str(game.community.river))

    print()
    print_border()


def get_player_count():
    player_count = 0

    while player_count < 2 or player_count > 8:
        try:
            player_count = int(input('How many players? (minimum 2, maximum 8): '))
        except ValueError:
            print('\tError: Please enter a number, like 2, 3, etc.')

    return player_count


def print_title():
    title = 'texas holdem poker'
    extra = ''
    if not len(title) % 2 == 0:
        extra = FILLER
    print_border()
    count = int((DISPLAY_WIDTH - len(title) - len(extra) - len(END * 2)) / 2)
    print(END + ' ' * count + title.upper() + ' ' * count + extra + END)
    print_border()


def print_border():
    count = int(DISPLAY_WIDTH - len(END * 2))
    print(END + FILLER * count + END)


def print_heading(heading):
    extra = ''
    if not len(heading) % 2 == 0:
        extra = FILLER
    count = int((DISPLAY_WIDTH - len(heading) - len(' ' * 2) - len(extra) - len(END)) / 2)
    print(END + FILLER * count + ' ' + heading.upper() + ' ' + FILLER * count + extra + END)
