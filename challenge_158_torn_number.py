#!/usr/bin/python

# DESCRIPTION
#
# I had the other day in my possession a label bearing the number 3 0 2 5 in large figures. This got
# accidentally torn in half, so that 3 0 was on one piece and 2 5 on the other. On looking at these pieces I
# began to make a calculation, when I discovered this little peculiarity. If we add the 3 0 and the 2 5
# together and square the sum we get as the result, the complete original number on the label! Thus, 30 added
# to 25 is 55, and 55 multiplied by 55 is 3025. Curious, is it not? 
#
# Now, the challenge is to find another number, composed of four figures, all different, which may be divided
# in the middle and produce the same result.
#
# BONUS
#
# Create a program that verifies if a number is a valid torn number.
#

def torn_numbers():
    ints_with_4_digit_squares = {
        'smallest': 32,
        'largest': 99
    }
 
    torns = []

    for number in range(ints_with_4_digit_squares['smallest'],  ints_with_4_digit_squares['largest'] + 1 ):
        square = number**2
        if is_torn_number(square):
               torns.append(square)

    return torns

def is_torn_number(number):
    return is_4_digit_number(number) and \
        has_unique_digits(number) and \
        (subnumber(number, 0, 2) + subnumber(number, 2, 4))**2 == number

def is_4_digit_number(number):
    return len(str(number)) == 4

def has_unique_digits(number):
    string = str(number)

    for character in string:
        if string.count(character) > 1:
            return False

    return True

def subnumber(number, start, stop):
    try:
        return int(str(number)[start:stop])
    except (ValueError):
        print 'ValueError: First argument must be an integer'

