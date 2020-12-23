#!/bin/env python3

import sys
import re
from pprint import pprint

def build_re(re, rule, tree, leaves, rule_11_n):
    if rule in leaves:
        re.append(leaves[rule])
        return
    assert(rule in tree) 
        
    for i, sub in enumerate(tree[rule]):
        re.append('|' if i > 0 else '(')
        for r in sub:
            build_re(re,r,tree,leaves, rule_11_n)
            
            # add rule 11 exception:
            if rule == 11:
                re.append('{')
                re.append(str(rule_11_n))    
                re.append('}')             
            
    re.append(')')
    
    # add rule 8 exception:
    if rule == 8:
        re.append('+')
    
def main():
        
    rule_tree = {}
    rule_tree_leaves = {}
    re_progs = None    

    # set this to be sufficiently high:
    max_rule_11_n = 10

    n_matches = 0
    
    for line in sys.stdin.readlines():
            
        if len(line.strip()) == 0:
            re_progs = []
            for n in range(1,max_rule_11_n+1):
                ruleset_re = ['^']
                build_re(ruleset_re,0,rule_tree,rule_tree_leaves,n)
                ruleset_re.append('$')
                re_progs.append(re.compile(''.join(ruleset_re)))
                #print(''.join(ruleset_re))
            
            continue      
        
        if re_progs is not None:
            for re_prog in re_progs:
                if re_prog.match(line.strip()):
                    print('Match:',line.strip())
                    n_matches += 1
                    break
            
            continue
        
        kv_pair = line.split(': ')
        rule = int(kv_pair[0].strip())
        rhs = kv_pair[1].strip()
        
        if '\"' in rhs:
            rule_tree_leaves[rule] = rhs[1:-1]
        else:
            substitutes = rhs.split(' | ')
            
            rule_tree[rule] = []
            for s in substitutes:
                seq = tuple(int(r) for r in s.strip().split(' '))
                rule_tree[rule].append(seq)
    
    print('# of matches:', n_matches)
    #pprint(rule_tree)
    #pprint(rule_tree_leaves)
    
             
    
if __name__ == '__main__':
    main()
