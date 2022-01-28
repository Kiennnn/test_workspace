#! /usr/bin/env python3

A = int(input())
origin_set = set(input().split())
N = int(input())
cmd_dict = {}
for i in range(N):
    command = input().split()
    update_set = set(input().split())
    if 'update' in command:
        origin_set.update(update_set)
    elif 'intersection_update' in command:
        origin_set.intersection_update(update_set)
    elif 'difference_update' in command:
        origin_set.difference_update(update_set)
    elif 'symmetric_difference_update' in command:
        origin_set.symmetric_difference_update(update_set)
    else:
        continue
my_list=[]
for i in origin_set:
    my_list.append(int(i))

print(sum(i for i in my_list))
