#!/bin/env python3

import sys
from pprint import pprint

def n_contained_bags(bag, 
        contained_bags, contained_bag_numbers, mem_dict):
    
    if bag in mem_dict:
        return mem_dict[bag]
    
    assert(bag in contained_bags)
     
    total = 0
    for c, n_c in zip(contained_bags[bag],contained_bag_numbers[bag]):
        cnt = n_contained_bags(c, contained_bags, contained_bag_numbers, mem_dict)
        total += n_c*(1+cnt)
    mem_dict[bag] = total
    return total

def main():
     
    contained_bags = {}
    contained_bag_numbers = {}
    mem_dict = {}

    for line in sys.stdin.readlines():
        line = line.strip()[:-1]
        line_tokens = line.split(' ')
        bag = ' '.join(tuple(line_tokens[:2]))
        contents = ' '.join(line_tokens[4:]).split(', ')
        contained_bags[bag] = []
        contained_bag_numbers[bag] = []        
        
        for item in contents:
            print(item)
            tokens = item.split(' ')
            if tokens[0] != 'no':
                number = int(tokens[0])
                contained_bag = ' '.join(tokens[1:3])
               
                contained_bags[bag].append(contained_bag)
                contained_bag_numbers[bag].append(number)
            
    pprint(contained_bags)
    pprint(contained_bag_numbers)

    total = n_contained_bags('shiny gold',contained_bags,contained_bag_numbers,mem_dict)
    pprint(mem_dict)
    print('# of bags:', total)
                   
if __name__ == '__main__':
    main()

