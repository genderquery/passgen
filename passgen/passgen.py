#!/usr/bin/env python

from argparse import ArgumentParser
from random import SystemRandom

_digits = '0123456789'
_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
_lowercase = 'abcdefghijklmnopqrstuvwxyz'
_symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
_ambiguous = 'B8G6I1l0OQDS5Z2'
_vowels = '01aeiouyAEIOUY'
_max_attempts = 100

def _passgen(length, charset, conditions=None):
    choice = SystemRandom().choice
    all_conditions_met = False
    password = None
    attempts = 0
    while not all_conditions_met:
        attempts += 1
        if attempts >= _max_attempts:
            break
        sbuffer = []
        while len(sbuffer) < length:
            c = choice(charset)
            sbuffer.append(c)
        password = ''.join(sbuffer)
        all_conditions_met = True
        for condition in conditions:
            if not condition(password):
                all_conditions_met = False
                password = None
                sbuffer = []
    return password
    
def _contains(a, b):
    if a is None or b is None:
        return False
    for c in a:
        if c in b:
            return True
    return False
    
def passgen(length=8, uppercase=True, digits=True, symbols=False, 
            ambiguous=True, vowels=True):
    conditions = []
    charset = _lowercase
    if uppercase:
        charset += _uppercase
        conditions.append(lambda s: _contains(s, _uppercase))
    if digits:
        charset += _digits
        conditions.append(lambda s: _contains(s, _digits))
    if symbols:
        charset += _symbols
        conditions.append(lambda s: _contains(s, _symbols))
    if not ambiguous:
        charset.translate(None, _ambiguous)
    if not vowels:
        charset.translate(None, _vowels)
    return _passgen(length, charset, conditions)
            
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--length', '-l', type=int, default=8)
    parser.add_argument('--uppercase', '-u', action='store_true')
    parser.add_argument('--digits', '-d', action='store_true')
    parser.add_argument('--symbols', '-s', action='store_true')
    parser.add_argument('--no-ambiguous', '-a', action='store_false', 
        dest='ambiguous', default=True)
    parser.add_argument('--no-vowels', '-v', action='store_false', 
        dest='vowels', default=True)
    args = parser.parse_args()
    password = passgen(**args.__dict__)
    print(password)
    
