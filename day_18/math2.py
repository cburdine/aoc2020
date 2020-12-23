#!/bin/env python3

import re
import sys

def main():
    
    total = 0

    for line in sys.stdin.readlines():

        opstack = ['$']
        line = re.sub('\(','( ',line)
        line = re.sub('\)',' )',line)

        tokens = line.strip().split(' ')
        for token in tokens:
            #print(opstack, token)
            if token == ')':  
                token = opstack.pop()
                while(opstack.pop() != '('):
                    v = opstack.pop()
                    #print(v, '-->', opstack)
                    token *= v
                 
            if token == '(':
                opstack.append(token)
            elif token == '+' or token == '*':
                opstack.append(token)
            else:
                if opstack[-1] == '$' or opstack[-1] == '(':
                    opstack.append(int(token))
                else:
                    op = opstack.pop()
                    assert(op == '+' or op == '*')
                    if op == '+':
                        value = opstack.pop()
                        value += int(token)
                    else:
                        opstack.append('*')
                        value = int(token)                    
                    opstack.append(value)
                           
        result = opstack.pop()
        while opstack.pop() != '$':
            result *= opstack.pop()
        print(result)
        total += result       
    
    print(total) 
                

if __name__ == '__main__':
    main()
