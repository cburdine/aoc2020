#!/bin/env python3

import sys
from pprint import pprint
import copy

ADJ_OFFSETS = [ 
    ( 0, 1),
    ( 1, 1),
    ( 1, 0),
    ( 1,-1),
    ( 0,-1),
    (-1,-1),
    (-1, 0),
    (-1, 1)
]

def count_seen_seats(r,c, seats):
    n_empty = 0
    n_occupied = 0

    for r_off, c_off in ADJ_OFFSETS:
        r_t = (r+r_off)
        c_t = (c+c_off)
        
        seat_seen = False
        while ((0 <= r_t < len(seats)) and 
               (0 <= c_t < len(seats[0])) and
               (seats[r_t][c_t] != 'L')):
            
            if seats[r_t][c_t] == '#':
                n_occupied += 1
                seen_seat = True
                break 
            r_t += r_off
            c_t += c_off
         
        if not seat_seen:
            n_empty += 1
    
    return n_empty, n_occupied

def n_occupied(seats):
    n_occupied = 0
    for row in seats:
        for s in row:
            n_occupied += 1 if s == '#' else 0

    return n_occupied

def timestep(seats):
    next_seats = copy.deepcopy(seats)
    stable = True
    
    for i in range(0,len(seats)):
        for j in range(0,len(seats[0])):
            empty_seen, occupied_seen = count_seen_seats(i,j,seats)
            if seats[i][j] == 'L' and occupied_seen == 0:
                next_seats[i][j] = '#'
                stable=False
            elif seats[i][j] == '#' and occupied_seen >= 5:
                next_seats[i][j] = 'L'
                stable=False

    return next_seats if not stable else None

def print_seats(seats):
    for row in seats:
        print(''.join(row))

def main():
    
    seats = list(map(list,sys.stdin.readlines()))
    for row in seats:
        row[-1] = ' '
    seats.append([' ']*len(seats[0]))
    #print_seats(seats)   
    
    while (seats := timestep(seats)) is not None:
        print(n_occupied(seats))
        #print_seats(seats)

if __name__ == '__main__':
    main()
