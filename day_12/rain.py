#!/bin/env python3

import sys

def b_sin(bearing):
    if bearing == 90:
        return 1;
    elif bearing == 270:
        return -1
    assert(bearing == 0 or bearing == 180)
    return 0

def b_cos(bearing):
    if bearing == 0:
        return 1
    elif bearing == 180:
        return -1
    assert(bearing == 90 or bearing == 270)
    return 0

def main():
    bearing = 0
    x = 0
    y = 0


    for line in sys.stdin.readlines():
        instr = line[0]
        num = int(line[1:])
        
        if instr == 'N':
            y += num
        elif instr == 'S':
            y -= num
        elif instr == 'E':
            x += num
        elif instr == 'W':
            x -= num
        elif instr == 'R':
            bearing = (bearing - num)%360
        elif instr == 'L':
            bearing = (bearing + num)%360
        elif instr == 'F':
            x += b_cos(bearing)*num
            y += b_sin(bearing)*num

    mdist = abs(x) + abs(y)
    print(x, y, ':', mdist)

if __name__ == '__main__':
    main()
