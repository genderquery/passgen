#!/usr/bin/env python

from random import SystemRandom

# TODO: add docstrings

_digits = '0123456789'
_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
_lowercase = 'abcdefghijklmnopqrstuvwxyz'
_symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
_ambiguous = 'B8G6I1l0OQDS5Z2'
_vowels = '01aeiouyAEIOUY'
_max_attempts = 100

def _generate(length, charset, conditions=None):
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
    
def generate(length=8, uppercase=True, digits=True, symbols=False, 
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
        charset = charset.translate(None, _ambiguous)
    if not vowels:
        charset = charset.translate(None, _vowels)
    return _generate(length, charset, conditions)
       
if __name__ == '__main__':
    pass
    
