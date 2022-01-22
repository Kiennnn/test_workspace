#! /usr/bin/env python3

N, M = map(int,input().split())
x='.|.'
top = int(N/2)  # upper half
mid = top + 1  # middle line

for i in range (1,N+1,1):
    if i <= top:
        print((x*(1 + (i-1)*2)).center(M,'-'))
    elif i == mid:
        print('WELCOME'.center(M,'-'))
    else:
        print((x*(1 + (top-1)*2 - 2*(i-mid-1))).center(M,'-'))

# 1 line
# for i in range(N):
#     print((x*(1+i*2)).center(M,'-') if i in range(int(N/2)) else 'WELCOME'.center(M,'-') if i==int(N/2) else (x*((int(N/2)-1)*2+1-(i-int(N/2)-1)*2)).center(M,'-'))
