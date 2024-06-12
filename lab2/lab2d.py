#!/usr/bin/env python3

import sys

#args = len(sys.argv)
#verify how many arguments there are calling the file; one argument counts.
#if there aren't precisely two more parameters check for three since calling the file with "./lab2d.py" counts as one argument, print a usage message.

if len(sys.argv) != 3:
    print('Usage: ./lab2d.py name age')
    sys.exit()

#make variables to hold argumts string objects are used to store arguments.
name = sys.argv[1]
age = sys.argv[2]

#print out
print('Hi ' + name + ', you are ' + age + ' years old.')