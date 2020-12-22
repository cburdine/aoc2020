#!/bin/env python3

import re
import sys
from pprint import pprint

def padded(bin_str, digits=36):
    if len(bin_str) >= digits:
        return bin_str
    return '0'*(digits-len(bin_str)) + bin_str

def bin2int(bin_str):
    x = 0
    for ch in bin_str:
        x = (x<<1)
        if(ch == '1'):
            x = (x|1)
    
    return x

def main():
    lines = sys.stdin.readlines()
    mask_idxs = []
    mask_values = []
    mem_dict = {}
    
    for line in lines:
        if line[1] == 'a':
            mask_str = line.split(' ')[2].strip()
            mask_idxs = []
            mask_values = []
            for i, char in enumerate(mask_str):
                if char == '0' or char == '1':
                    mask_idxs.append(i)
                    mask_values.append(char)
        else:
            tokens = re.split('[\[\]\s]', line)
            addr = int(tokens[1])
            val_str = list(padded(format(int(tokens[4]),'b')))
             
            for i, v in zip(mask_idxs,mask_values):
                val_str[i] = v
            
            mem_dict[addr] = ''.join(val_str)
    
    total = sum(bin2int(v) for v in mem_dict.values())

    pprint(mem_dict)
    print('Total:', total)
                
    
                

if __name__ == '__main__':
    main()
