#!/bin/env python3

import sys
import re


def is_valid(val, ranges):
    for r in ranges:
        if val in range(*r[0]) or val in range(*r[1]):
            return True
    return False

def match_field_values(vals, ranges):
    matched_ranges = set()
    for i, r in enumerate(ranges):
        matches = True
        for val in vals:
            if val not in range(*r[0]) and val not in range(*r[1]):
                matches = False
                break
        if matches:
            matched_ranges.add(i)

    return matched_ranges
            

def main():
    lines = sys.stdin.readlines()
    ranges = []
    fields = []

    l = 0
    # read 'fields':
    while len(lines[l].strip()) > 0:
        kv_pair = lines[l].strip().split(':')
        fields.append(kv_pair[0])
        range_list = kv_pair[1]
        range_strs = re.split('[-\s]',range_list.strip())
        ranges.append([
            (int(range_strs[0]),int(range_strs[1])+1),
            (int(range_strs[3]),int(range_strs[4])+1)
        ])
        l += 1
    
    # read tickets:
    l += 2
    valid_tickets = []
    your_ticket = [ int(s.strip()) for s in lines[l].split(',')]
    print('your ticket:', your_ticket)
    l += 3
    for line in lines[l:]:
        ticket = [int(s.strip()) for s in line.split(',')]
        
        valid = True
        for val in ticket:
            if not is_valid(val,ranges):
                valid = False
                break
        
        if valid:
            valid_tickets.append(ticket)     
     
    assert(len(valid_tickets) > 0)
    match_sets = []
    for f in range(len(valid_tickets[0])):
        values = [ t[f] for t in valid_tickets ]
        match_sets.append(match_field_values(values, ranges))
    
    # NOTE: here we exploit the structure of the input data:
    match_set_idx = sorted(list(range(0,len(match_sets))),key=lambda i : len(match_sets[i]))
    #match_sets.sort(key=lambda s : len(s))    
   
    for i, s_ind in enumerate(match_set_idx):
        for j in range(i+1,len(match_set_idx)):
            match_sets[match_set_idx[j]] -= match_sets[s_ind]
    
    # maps given index -> field index
    field_assignments = [ next(iter(s)) for s in match_sets ]
    print('field assignments:')
    print(field_assignments)
    
    answer = 1
    for i, val in enumerate(your_ticket):
        if 'departure' in fields[field_assignments[i]]:
            print(fields[field_assignments[i]], ':',val)
            answer *= val
    print('Answer:',answer)

if __name__ == '__main__':
    main()
