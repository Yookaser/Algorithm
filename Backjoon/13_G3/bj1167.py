# 1167. 트리의 지름

def dfs():
    
    return

import sys

input = sys.stdin.readline
V = int(input())
line = [[] for _ in range(V+1)]

for _ in range(V):
    arr = list(map(int, input().split()))
    visited = {}
    for i in range(1, len(arr)-1, 2):
        if i == -1:
            break
        line[arr[0]].append((arr[i], arr[i+1]))


"""
6
1 6 1 3 2 -1
2 3 3 5 4 -1
3 1 4 5 5 -1
4 3 8 -1
5 2 6 -1
6 3 3 -1
"""