#!/usr/bin/python3


def isValidShortForm(short_form):
    return True


def isValidLongForm(long_form):
    return True


def isValidFlag(flag):
    return isValidShortForm(flag['short_form']) and isValidLongForm(flag['long_form'])


def collectFlags(number, flags={}):
    if number <= 0:
        return flags

    flag_definition = input()
    flag_forms = flag_definition.split(':', 1)
    flag = {
        'short_form': flag_forms[0],
        'long_form': flag_forms[1]
    }

    if isValidFlag(flag):
        flags.update(flag)
        return collectFlags(number - 1, flags)
    else:
        print('The short-form definition is invalid.')
        try_again = input('Try again? (y/n): ') == 'y'

        if try_again:
            return collectFlags(number, flags)
        else:
            return flags

number_of_flags = int(input('Enter number of flags: '))
print('Enter ', number_of_flags, ' short-form definintions in the format shortform:longform, e.g. f:force.')

print('Collected flags: ', collectFlags(number_of_flags))

commandline = input('Enter a line of flags and other parameters: ')
