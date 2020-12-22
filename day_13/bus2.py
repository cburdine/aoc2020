#!/bin/env python3

import sys

def modulo_inv(rem, div):
    r_cur = rem
    r_prev = div
    s_prev = 0
    s_cur = 1
    
    while (r_next := r_prev%r_cur) != 0:
        q = r_prev//r_cur
        r_cur, r_prev = r_next, r_cur
        s_prev, s_cur = s_cur, s_prev - q*s_cur
    
    assert(r_cur == 1)
    return s_cur % div
 
def solve_crt(rems, divisors):
    N = 1
    for d in divisors:
        N *= d
    
    x = 0
    for r,d in zip(rems,divisors):
        n = N//d
        x += r*n*modulo_inv(n,d)
    
    return x % N

def main():
    lines = sys.stdin.readlines()
    start = int(lines[0])
    bus_nums = []
    departure_rems = []
    for i, bus in enumerate(lines[1].split(',')):
        if bus != 'x':
            bus_num = int(bus)
            bus_nums.append(bus_num)
            departure_rems.append(-i)
    
    print('remainders:\n',departure_rems)
    print('bus ids:\n',bus_nums)

    x = solve_crt(departure_rems, bus_nums)
    print('timestamp:', x)
    for r,d in zip(departure_rems, bus_nums):
        print('got: ', x%d, ' expected: ', r%d)
     
    
if __name__ == '__main__':
    main()
