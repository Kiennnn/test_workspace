#! /usr/bin/env python3
import string

def reverse_list(my_list):
    my_list.reverse()
    return my_list

def print_rangoli(size):
    # your code goes here
    alphabet = list(string.ascii_lowercase)
    line_number = size*2 - 1
    for i in range (line_number):
        if i < size:
            line = ''.join(reverse_list(alphabet[(size-i):(size)])) + alphabet[size-1-i] + ''.join(alphabet[(size-i):(size)])
        else:
            line = ''.join(reverse_list(alphabet[(i-size+2):(size)])) + alphabet[i-size+1] + ''.join(alphabet[(i-size+2):(size)])

        joined_line = '-'.join(line)
        print(joined_line.center(4*size-3,'-'))  # 2n-1 letters plus 2n-2 '-' characters

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)