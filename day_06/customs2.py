#!/bin/env python3

import sys

def main():
    
    counts = 0
    questions = None
    for line in sys.stdin.readlines():
        line = line.strip()
        if len(line) > 0:
            if questions is None:
                questions = set(line)
            else:
                questions &= set(line)
        else:
            counts += len(questions)
            print('Group:', len(questions))
            questions = None 
    
    if questions is not None:
        print('Group:', len(questions))
        counts += len(questions)

    print('Counts: ', counts)

if __name__ == '__main__':
    main()
