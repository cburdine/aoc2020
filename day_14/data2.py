#!/bin/env python3

import re
import sys
from pprint import pprint

ADDR_LEN = 36

def get_mem_addrs(addr, mask, floats):
    mem_addrs = [ addr|mask ]
    for float_mask in floats:
        next_mem_addrs = []
        for ma in mem_addrs:
                next_mem_addrs.append(float_mask|ma)
                next_mem_addrs.append((~float_mask)&ma)
        mem_addrs = next_mem_addrs
    
    return mem_addrs

def main():
    lines = sys.stdin.readlines()
    mask_floats = []
    mask = 0
    mem_dict = {}
    
    for line in lines:
        if line[1] == 'a':
            mask_str = line.split(' ')[2].strip()
            mask_floats = []
            mask = 0
            for i, char in enumerate(mask_str):
                mask = (mask<<1)
                if char == 'X':
                    mask_floats.append(1<<(ADDR_LEN-(i+1)))
                else:
                    mask = (mask|int(char))
            #print('MASK:')
            #pprint(format(mask,'b'))
            #pprint([ format(m,'b') for m in mask_floats])
        
        else:
            tokens = re.split('[\[\]\s]', line)
            addr = int(tokens[1])
            val = int(tokens[4])
            mem_addrs = get_mem_addrs(addr,mask,mask_floats)
            
            #print('MEMORY Write:', val)
            #pprint(format(addr,'b'))
            #pprint([format(a,'b') for a in sorted(mem_addrs)])
            
            for mem_addr in mem_addrs:
                mem_dict[mem_addr] = val
    
    #pprint(mem_dict)                
    total = sum(mem_dict.values())
    print('Total:', total)

if __name__ == '__main__':
    main()
