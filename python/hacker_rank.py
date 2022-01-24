#! /usr/bin/env python3

def print_formatted(number):
    # your code goes here
    len = int(number).bit_length()
    for i in range (1, number+1, 1):
        d = str(i).upper()
        o = str(oct(i)).upper()
        h = str(hex(i)).upper()
        b = str(bin(i)).upper()
        ls = [d.rjust(len), o[2:].rjust(len), h[2:].rjust(len), b[2:].rjust(len)]
        print(*ls)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)