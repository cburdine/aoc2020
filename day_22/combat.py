#!/bin/env python3

import sys
from collections import deque

def main():
    
    player_deck = deque()
    crab_deck = deque()
     
    lines = sys.stdin.readlines()
    sink = player_deck
    for line in lines:
        if len(line.strip()) == 0:
            sink = crab_deck
        elif line[0] != 'P':
            sink.append(int(line))

    print(player_deck)
    print(crab_deck)

    while len(player_deck) > 0 and len(crab_deck) > 0:
        cards = [ player_deck.popleft(), crab_deck.popleft() ]
        if cards[0] > cards[1]:
            player_deck.extend(sorted(cards,reverse=True))
        else:
            crab_deck.extend(sorted(cards, reverse=True))

    print(player_deck)
    print(crab_deck)


    if len(player_deck) > 0:
        winner = player_deck
    else:
        winner = crab_deck

    result = sum(c*(len(winner)-i) for i, c in enumerate(winner))
    print(result)
        

if __name__ == '__main__':
    main()        
