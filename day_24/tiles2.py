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

def n_black_neighbors(tile, grid):
    n_black = 0
    for off in DIRECTIONS.values():
        adj_tile = (tile[0]+off[0],tile[1]+off[1]) 
        if adj_tile in grid and grid[adj_tile]:
            n_black += 1

    return n_black

def new_adj_tiles(tile, grid):
    new_adjs = []
    for off in DIRECTIONS.values():
        adj_tile = (tile[0]+off[0],tile[1]+off[1])
        if adj_tile not in grid:
            new_adjs.append(adj_tile)
        
    return new_adjs

def timestep(grid):
    white_adjs = set()
    next_grid = {}
    
    for tile in grid.keys():
        white_adjs.update(new_adj_tiles(tile,grid))
        
    # update tiles in grid:
    for tile, black in grid.items():
        black_neighbors = n_black_neighbors(tile, grid)
        if black and (0 < black_neighbors <= 2):
            next_grid[tile] = True
        elif (not black) and (black_neighbors == 2):
            next_grid[tile] = True
    
    for tile in white_adjs:
        black_neighbors = n_black_neighbors(tile,grid)
        if black_neighbors == 2:
            next_grid[tile] = True
            
    return next_grid

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

    
    
    for n in range(100):
        grid = timestep(grid) 
        black_tiles = [ pos for pos in grid.keys() if grid[pos] ]   
        print('Day', n+1, ':', len(black_tiles))
    


if __name__ == '__main__':
    main()
