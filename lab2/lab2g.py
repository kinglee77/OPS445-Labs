#!/usr/bin/env python3

#author: Lia Brown
#author ID: lbrown63
#Date Created 2024/06/05


import sys

#number = len(sys.argv)

#if we dont have argument, used 3
if len(sys.argv) !=2:
    timer = 3
else:
    #get the timer number by user
    timer = int(sys.argv[1])
#created a countdown with while loop
while timer !=0:
    print(timer)
    timer = timer -1
print ('blast off!')