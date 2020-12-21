#!/bin/env python3

import sys
from pprint import pprint

def mark_bags(bag, marked_set, containing_bags):
    for cont_bag in containing_bags[bag]:
        marked_set.add(cont_bag)
        if cont_bag in containing_bags: 
            mark_bags(cont_bag, marked_set, containing_bags)

def main():
     
    containing_bags = {}
    containing_bag_numbers = {}
    marked_set = set() 

    for line in sys.stdin.readlines():
        line = line.strip()[:-1]
        line_tokens = line.split(' ')
        bag = ' '.join(tuple(line_tokens[:2]))
        contents = ' '.join(line_tokens[4:]).split(', ')
        
        for item in contents:
            #print(item)
            tokens = item.split(' ')
            if tokens[0] != 'no':
                number = int(tokens[0])
                bag_content = ' '.join(tokens[1:3])
               
                if bag_content not in containing_bags:
                    containing_bags[bag_content] = []
                    containing_bag_numbers[bag_content] = []

                containing_bags[bag_content].append(bag)
                containing_bag_numbers[bag_content].append(number)

    #pprint(containing_bags)
    #pprint(containing_bag_numbers)
    
    mark_bags('shiny gold', marked_set, containing_bags)
    print('# of bags:', len(marked_set))
                        
if __name__ == '__main__':
    main()

