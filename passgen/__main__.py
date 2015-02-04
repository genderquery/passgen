#!/usr/bin/env python

from argparse import ArgumentParser
from passgen import generate

# TODO: add help text

def main():
    parser = ArgumentParser()
    parser.add_argument('--length', '-l', type=int, default=8)
    parser.add_argument('--uppercase', '-u', action='store_true')
    parser.add_argument('--digits', '-d', action='store_true')
    parser.add_argument('--symbols', '-s', action='store_true')
    parser.add_argument(
        '--no-ambiguous', '-a', action='store_false', dest='ambiguous',
         default=True)
    parser.add_argument(
        '--no-vowels', '-v', action='store_false', dest='vowels', 
        default=True)
    args = parser.parse_args()
    password = generate(**args.__dict__)
    print(password)

if __name__ == '__main__':
    __main__()
