#!/bin/env python3

import sys
def adj_pts(pt):
    
    pts_list = []
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                if (i,j,k) != (0,0,0):
                    pts_list.append((pt[0]+i,pt[1]+j,pt[2]+k))

    return pts_list

def partition_pts(pt_list, active_pts):
    active = []
    inactive = []
    for pt in pt_list:
        if pt in active_pts:
            active.append(pt)
        else:
            inactive.append(pt)

    return active, inactive

def main():
    
    active_cubes = set()
    n_steps = 6
    lines = sys.stdin.readlines()

    for i, line in enumerate(lines):
        for j, ch in enumerate(line.strip()):
            if ch == '#':
                active_cubes.add((i,j,0))
    
    for t in range(n_steps):
        inactive_cubes = set()
        next_active_cubes = set()
        for pt in active_cubes:
            neighbors = adj_pts(pt)
            active_neighbors, inactive_neighbors = partition_pts(neighbors,active_cubes)
            
            if 2 <= len(active_neighbors) <= 3:
                next_active_cubes.add(pt)
            inactive_cubes.update(inactive_neighbors)
        
        for pt in inactive_cubes:
            neighbors = adj_pts(pt)
            active_neighbors, _ = partition_pts(neighbors,active_cubes)
            if len(active_neighbors) == 3:
                next_active_cubes.add(pt)
            
        print(f'[{t+1}]: {len(active_cubes)} -> {len(next_active_cubes)}')
        active_cubes = next_active_cubes
        
if __name__ == '__main__':
    main()
