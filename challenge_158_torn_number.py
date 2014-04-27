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
    '''
    Returns list of torn numbers.
    '''
    smallest_4_digit_square = 1024
    largest_4_digit_square = 9801
    
    torns = []
    
    for number in range( smallest_4_digit_square,  largest_4_digit_square + 1): 
        if is_torn_number( number ):
               torns.append( number )
    
    return torns

def is_torn_number( number ):
    '''
    Returns True if parameter number (int) is a torn number; False, otherwise.
    '''
    if is_4_digit_number( number ) and has_unique_digits( number ) :
        first = number / 100 # First two digits as a number.
        second = number - ( first * 100 ) # Second two digits as a number.
        
        if ( first + second )**2 == number:
            return True
    
    return False

def is_4_digit_number( number ):
    '''
    Returns True if parameter number (int) contains only four digits; False, otherwise.
    '''
    return len( str( number ) ) == 4

def has_unique_digits( number ):
    '''
    Returns True if all digits of parameter number (int) are unique; False, otherwise.
    '''
    string = str( number )
    for c in string:
        if string.count( c ) > 1:
            return False
    
    return True
    