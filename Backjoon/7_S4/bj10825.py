# 10825. 국영수

from sys import stdin


input = stdin.readline
N = int(input())
A = sorted([tuple(input().split()) for _ in range(N)], key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))  # 기준에 따라 정렬

for s in A: 
    print(s[0])
