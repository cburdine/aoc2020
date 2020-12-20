#!/bin/env python3

import sys

def main():
    
    counts = 0
    questions = set()
    for line in sys.stdin.readlines():
        line = line.strip()
        if len(line) > 0:
            questions |= set(line)
        else:
            counts += len(questions)
            print('Group:', len(questions))
            questions = set() 
    
    print('Group:', len(questions))
    counts += len(questions)

    print('Counts: ', counts)

if __name__ == '__main__':
    main()
