#! /usr/bin/env python3
A = set(input().split())
n = int(input())
answer = True
for i in range(n):
    N = set(input().split())
    diff = A.difference(N)
    if len(diff) > 0 and A.intersection(N) == N:
        continue
    else:
        answer = False
        break
print(answer)