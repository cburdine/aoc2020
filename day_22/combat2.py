#!/bin/env python3

import sys
from collections import deque
from itertools import islice
from copy import copy

combat_cache = {}

def combat(player_deck, crab_deck):
     
    cache_k = (tuple(player_deck),tuple(crab_deck))
    if cache_k in combat_cache:
        return combat_cache[cache_k]

    prev_rounds = set()
    k = None
    while len(player_deck) > 0 and len(crab_deck) > 0:
    
        if (k := (tuple(player_deck),tuple(crab_deck))) in prev_rounds:
            return 0
        prev_rounds.add(k)
         
        cards = (player_deck.popleft(), crab_deck.popleft())
        if len(player_deck) >= cards[0] and len(crab_deck) >= cards[1]:
            winner = combat(
                deque(islice(player_deck,0,cards[0])),
                deque(islice(crab_deck,0,cards[1]))
            )
        else:
            winner = 0 if cards[0] > cards[1] else 1
        
        if winner == 0:
            player_deck.extend(cards)
        else:
            crab_deck.extend(reversed(cards))

    print('cache size:',len(combat_cache))    
    result = 0 if len(player_deck) > 0 else 1
    combat_cache[cache_k] = result
    return result
            

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
    
    player = combat(player_deck, crab_deck)
    win_deck = player_deck if len(player_deck) > 0 else crab_deck

    print('Winning player:', player)
    print('Winning deck:', win_deck)

    result = sum(c*(len(win_deck)-i) for i, c in enumerate(win_deck))
    print(result)
        

if __name__ == '__main__':
    main()        
