#! /usr/bin/env python3

from collections import Counter as cnt

K = int(input())
room_list = input().split()
room_set = set(room_list)  # to eliminate duplicate elements
room_without_captain = set((cnt(room_list)-cnt(room_set)).elements())  # remain family's rooms
captain_room = list(room_set.difference(room_without_captain))
print(captain_room[0])