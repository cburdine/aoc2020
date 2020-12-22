#!/bin/env python3

import sys

def is_valid(val, ranges):
    for r in ranges:
        if val in range(*r):
            return True
    return False

def main():
    lines = sys.stdin.readlines()
    ranges = []

    l = 0
    # read 'fields':
    while len(lines[l].strip()) > 0:
        range_list = lines[l].strip().split(':')[1]
        range_strs = range_list.strip().split(' ')
        for range_str in range_strs:
            if '-' in range_str:
                tokens = range_str.split('-')
                low = int(tokens[0])
                high = int(tokens[1])+1
                ranges.append((low,high))
        l += 1
            
    # read tickets:
    l += 2
    your_ticket = [ int(s.strip()) for s in lines[l].split(',')]
    l += 3

    err_rate = 0

    for line in lines[l:]:
        ticket = [int(s.strip()) for s in line.split(',')]
        for val in ticket:
            if not is_valid(val,ranges):
                err_rate += val            

    print('Error rate:', err_rate)
        

    
    

if __name__ == '__main__':
    main()
