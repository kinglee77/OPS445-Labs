#!/usr/bin/env python3

# Author ID: lbrown63

import subprocess

def free_space():
    #this command when run it, to get free disk space on the root directory
    exe = subprocess.Popen(['df -h | grep "/$" | awk \'{print $4}\''], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #communicate with the process to get commands output
    output = exe.communicate()
    #return the stdout data, decode it from bytes to a UTF-8 string, and strip any surrounding whitespace-newline characters
    return output[0].decode('utf-8').strip()

if __name__ == '__main__':
    #print the free space size
    print(free_space())