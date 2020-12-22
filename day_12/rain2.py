#!/bin/env python3

import sys

def rotate_l(x,y,degrees):
    for _ in range(degrees//90):
        x, y = -y, x
    return x, y
        
def rotate_r(x,y,degrees):
    for _ in range(degrees//90):
        x, y = y, -x
    return x, y

def main():
    bearing = 0
    wp_x = 10
    wp_y = 1
    x = 0
    y = 0


    for line in sys.stdin.readlines():
        instr = line[0]
        num = int(line[1:])
        
        if instr == 'N':
            wp_y += num
        elif instr == 'S':
            wp_y -= num
        elif instr == 'E':
            wp_x += num
        elif instr == 'W':
            wp_x -= num
        elif instr == 'R':
            wp_x, wp_y = rotate_r(wp_x, wp_y, num)
        elif instr == 'L':
            wp_x, wp_y = rotate_l(wp_x, wp_y, num)
        elif instr == 'F':
            x += wp_x*num
            y += wp_y*num
 
    mdist = abs(x) + abs(y)
    print(x, y, ':', mdist)

if __name__ == '__main__':
    main()
