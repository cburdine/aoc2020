#!/bin/env python3

import sys

def move(current, cups):
    
    c_ind = cups.index(current) 
    rem = [ cups[i%len(cups)] for i in range(c_ind+1,c_ind+4) ]
    dest = (current-1)%len(cups)
    while dest in rem:
        dest = (dest-1)%len(cups)
    tmp = [ c for c in cups if c not in rem ]
    split_ind = tmp.index(dest)+1

    #print(rem)
    
    cups = tmp[:split_ind]
    cups.extend(rem)
    cups.extend(tmp[split_ind:])    

    cur_next = cups[(cups.index(current)+1)%len(cups)]

    return cur_next, cups

def main():
    lines = sys.stdin.readlines()
    cups = [ int(ch)-1 for ch in lines[0].strip() ]
    
    current = cups[0]
    for _ in range(100):
        current, cups = move(current,cups)
        #print(cups)


    current = cups.index(0)
    cups = [ cups[(current+i)%len(cups)] for i in range(1,len(cups)) ]
    result = ''.join(str(c+1) for c in cups)

    print(result)
    

if __name__ == '__main__':
    main()
