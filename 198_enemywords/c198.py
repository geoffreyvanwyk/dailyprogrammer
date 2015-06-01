def enemyWords(left, right):
    left_remains = left
    right_remains = right
    result = {}
    cache = ''

    for c in left:
        if c in right and not (c in cache):
            if right.count(c) > left.count(c):
                right_remains = right_remains.replace(c, '', left.count(c))
                left_remains = left_remains.replace(c, '', right.count(c) - left.count(c))
            elif right.count(c) < left.count(c):
                right_remains = right_remains.replace(c, '', left.count(c) - right.count(c))
                left_remains = left_remains.replace(c, '', right.count(c))
            else:
                right_remains = right_remains.replace(c, '', left.count(c))
                left_remains = left_remains.replace(c, '', right.count(c))

            cache += c

    result['remains'] = left_remains + right_remains

    if len(left_remains) > len(right_remains):
        result['winner'] = 'left'
    elif len(left_remains) < len(right_remains):
        result['winner'] = 'right'
    else:
        result['winner'] = 'tie'

    return result
