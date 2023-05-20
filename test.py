#!/bin/env python3
import sys

def main(args):
    print("Hello World")


if __name__ == '__main__':
    try:
        print("\033[0;32m", end='')
        sys.exit(main(sys.argv))
    except Exception as exp:
        print(f'\033[1;31m{exp}\033[0m', file=sys.stderr, sep='')
        # raise exp  # Uncomment to debug code
    finally:
        print('\033[0m', end='')
