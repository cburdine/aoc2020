#!/bin/env python3

from copy import copy
import sys

def main():
    lines = sys.stdin.readlines()
    ingredients = []
    allergens = []
    assignments = {}

    all_ingredients = set()
    all_allergens = set()

    for line in lines:
        kv_pair = line.strip().split('(contains ')
        i_set = set(kv_pair[0].strip().split(' '))
        a_set = set(kv_pair[1][:-1].strip().split(', '))
        ingredients.append(i_set)
        allergens.append(a_set)
        all_ingredients.update(i_set)
        all_allergens.update(a_set)
   
    print(ingredients)
    print(allergens)
 
    allergen_map = {} 
    for i, a in zip(ingredients,allergens):
        for al in a:
            if al not in allergen_map:
                allergen_map[al] = copy(i)
            else:
                allergen_map[al] &= i
    
    print(allergen_map)

    # determine all allergenic ingredients:
    done = False
    while not done:
        done = True
        for al in allergen_map:
            if len(allergen_map[al]) == 1:
                ing = next(iter(allergen_map[al]))
                assignments[ing] = al
                for al_oth in allergen_map:
                    if al_oth != al and ing in allergen_map[al_oth]:
                        allergen_map[al_oth].remove(ing)
                        done = False
        print(allergen_map)

    # determine any non-allergenic ingredients:
    for ing in all_ingredients:
        safe_ing = True                        
        for al, ing_set in allergen_map.items():
            if ing in ing_set:
               safe_ing = False

        if safe_ing:
            assignments[ing] = None


    # count occurrences of safe ingredients:
    safe_ingredients = [ i for i in assignments if assignments[i] is None ]
    n_occurrences = 0
    
    for si in safe_ingredients:
        for i_set in ingredients:
            if si in i_set:
                n_occurrences += 1

    print('Occurrences of safe ingredients:', n_occurrences)

    

if __name__ == '__main__':
    main()
