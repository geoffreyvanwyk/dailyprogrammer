from c198 import enemyWords


def testEnemyWords():
    assert enemyWords('hat', 'cat') == {'remains': 'hc', 'winner': 'tie'}
    assert enemyWords('miss', 'hiss') == {'remains': 'mh', 'winner': 'tie'}
    assert enemyWords('because', 'cause') == {'remains': 'be', 'winner': 'left'}
    assert enemyWords('hello', 'below') == {'remains': 'hlbw', 'winner': 'tie'}
    assert enemyWords('rekt', 'pwn') == {'remains': 'rektpwn', 'winner': 'left'}
    assert enemyWords('combo', 'jumbo') == {'remains': 'coju', 'winner': 'tie'}
    assert enemyWords('critical', 'optical') == {'remains': 'ricop', 'winner': 'left'}
    assert enemyWords('isoenzyme', 'apoenzyme') == {'remains': 'isap', 'winner': 'tie'}
    assert enemyWords('tribesman', 'brainstem') == {'remains': '', 'winner': 'tie'}
    assert enemyWords('blames', 'nimble') == {'remains': 'asni', 'winner': 'tie'}
    assert enemyWords('yakuza', 'wizard') == {'remains': 'ykuawird', 'winner': 'tie'}
    assert enemyWords('longbow', 'blowup') == {'remains': 'ngoup', 'winner': 'left'}
