#!/bin/env python3

import sys

def main():
    lines = sys.stdin.readlines()
    start = int(lines[0])
    arrival_times = []
    ids = []
    for bus in lines[1].split(','):
        if bus != 'x':
            bus_num = int(bus)
            arrival_times.append(bus_num - (start%bus_num))
            ids.append(bus_num)
            #print(bus_num, arrival_times[-1])

    result = min(zip(arrival_times,ids))
    print('(wait_time, id): ', result)       
    print('product:', result[0]*result[1])    

if __name__ == '__main__':
    main()
