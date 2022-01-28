#! /usr/bin/env python3

n = int(input())
eng_set = set(input().split())
b = int(input())
fre_set = set(input().split())
inter_set = eng_set.intersection(fre_set)
print(len(inter_set))