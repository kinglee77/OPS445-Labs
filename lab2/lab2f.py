#!/usr/bin/env python3

#author: Lia Brown
#author ID: lbrown63
#Date Created 2024/06/05


import sys

#give the timer object's value of int(sys.argv[1]).
timer = int(sys.argv[1])

#while loop that keeps going until timer equals 0
while timer !=0:
    print(timer)
    timer -= 1
print("blast off!") 