#!/bin/env python3

import sys
import re

REQUIRED_KEYS = { 
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
}

VALID_HGT_FMTS = { 'in', 'cm' }

HCL_RE = '^#[0-9a-f]{6}$'

VALID_ECLS = {
    'amb',
    'blu',
    'brn',
    'gry',
    'grn',
    'hzl',
    'oth'
}

PID_RE = '^[0-9]{9}$'

def valid(cred):
    
    if not REQUIRED_KEYS.issubset(cred.keys()):
        return False

    try:
        byr = int(cred['byr'])
        iyr = int(cred['iyr'])
        eyr = int(cred['eyr']) 
        hgt = int(cred['hgt'][:-2])
        hgt_fmt = cred['hgt'][-2:]
        hcl = cred['hcl']
        ecl = cred['ecl']
        pid = cred['pid']
        
        if byr < 1920 or  2002 < byr:
            return False
        if iyr < 2010 or 2020 < iyr:
            return False
        if eyr < 2020 or 2030 < eyr:
            return False

        if hgt_fmt not in VALID_HGT_FMTS:
            return False
        if hgt_fmt == 'cm' and (hgt < 150 or 193 < hgt):
            return False
        if hgt_fmt == 'in' and (hgt < 59 or 76 < hgt):
            return False
        
        if re.search(HCL_RE,hcl) is None:
            return False

        if ecl not in VALID_ECLS:
            return False
        
        if re.search(PID_RE, pid) is None:
            return False

    except Exception as e:
        print(e, '\nparse error:\n', cred)        
        return False

    return True

def main():

    n_seen = 0    
    n_valid = 0
    cred = {}

    for line in sys.stdin.readlines():
        line = line.strip()
        if len(line) <= 0:
            n_seen += 1
            if valid(cred):
                n_valid += 1
            cred = {}
        else:
            for pair in line.split(' '):
                #print(pair, pair.split(':'))
                key, value = pair.split(':')
                cred[key] = value
    
    n_seen += 1
    if valid(cred):
        n_valid += 1
    
    print('# seen:', n_seen)
    print('# valid:', n_valid)

if __name__ == '__main__':
    main()
