#!/bin/env python3

import sys
import math

def discrete_log(x, base):
    p = base
    e = 1
    while p != x:
        p = (p*base)%20201227
        e += 1
    
    return e

def main():
    
    lines = sys.stdin.readlines()
    card_pub = int(lines[0].strip())
    door_pub = int(lines[1].strip())

    card_loop = discrete_log(card_pub,7)
    door_loop  = discrete_log(door_pub,7)

    print(card_pub, '-->', card_loop)
    print(door_pub, '-->', door_loop)

    print(pow(card_pub, door_loop, 20201227))
    print(pow(door_pub, card_loop, 20201227))

    
    
if __name__ == '__main__':
    main()
