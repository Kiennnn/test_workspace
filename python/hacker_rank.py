#! /usr/bin/env python3

import os

# Complete the solve function below.
def solve(s):
    s = list(s)
    if s[0].isalpha():
        s[0] = s[0].upper()
    for i in range(len(s)):
        if s[i] == ' ':
            s[i+1] = s[i+1].upper()
    s = ''.join(s)
    return s

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
