#! /usr/bin/env python3

from collections import Counter

shoes = int(input())
shoe_sizes = list(map(int, input().split()))
size_counter = Counter(shoe_sizes)
customers= int(input())
total_price = 0
for i in range(customers):
    shoe_size, price = map(int, input().split())
    if shoe_size in shoe_sizes and size_counter[shoe_size] != 0:
        total_price += price
        size_counter[shoe_size] -= 1
    else:
        continue
print(total_price)