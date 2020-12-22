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

def count_adj_seats(r,c, seats):
    n_empty = 0
    n_occupied = 0

    for r_off, c_off in ADJ_OFFSETS:
        r_t = (r+r_off)%len(seats)
        c_t = (c+c_off)%len(seats[0])
        
        seat = seats[r_t][c_t]
        if(seat == '#'):
            n_occupied += 1 
        else:
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
            empty_adj, occupied_adj = count_adj_seats(i,j,seats)
            if seats[i][j] == 'L' and empty_adj >= 8:
                next_seats[i][j] = '#'
                stable=False
            elif seats[i][j] == '#' and occupied_adj >= 4:
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
