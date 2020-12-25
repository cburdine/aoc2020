#!/bin/env python3

import sys

DIRECTIONS = {
    'e':  (1,0),
    'w':  (-1,0),
    'sw': (0, -1),
    'nw': (-1, 1),
    'se': (1, -1),
    'ne': (0, 1)
}

def main():
    
    grid = {}
    
    for line in sys.stdin.readlines():
        dir_key = ''
        pos_r, pos_c = 0, 0
         
        for ch in line.strip():
            dir_key += ch
            if ch == 'e' or ch == 'w':
                off = DIRECTIONS[dir_key]
                pos_r, pos_c = pos_r+off[0], pos_c+off[1]
                dir_key = ''
       
        if (pos_r,pos_c) not in grid:
            grid[(pos_r,pos_c)] = True
        else:
            grid[(pos_r,pos_c)] ^= True

     
    black_tiles = [ pos for pos in grid.keys() if grid[pos] ]

    print('# of black tiles: ', len(black_tiles))
            
            
    


if __name__ == '__main__':
    main()
