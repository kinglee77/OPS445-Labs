#!/usr/bin/env python3
# Author ID: lbrown63


def is_digits(sobj):
       #i made set digit for lookup
    digits = set('0123456789')
        #i go every character in the string once
    for char in sobj:
        #i check if the character is not digit
        if char not in digits:
            #return false if a non digit character is show
            return False
    #return true if the loop finished without showing any non digt characters    
    return True


if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')