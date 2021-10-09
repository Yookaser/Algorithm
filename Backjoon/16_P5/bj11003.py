# 11003. 최솟값 찾기

# heapq로 풀면 시간초과가 발생함
# q에 들어온 숫자가 많을수록 정렬하는데 오랜 시간이 걸리기 때문
# 따라서 heapq가 아닌 deque로 heapq와 비슷하게 작동하도록 구현
# 즉, 맨 앞에만 계속 최솟값이 오도록 구현하면 됨
from sys import stdin
from collections import deque


input = stdin.readline
N, L = map(int, input().split())
A = list(map(int, input().split()))
D = [0] * N
q = deque()

for i, v in enumerate(A):
    while q and q[-1][0] >= v: q.pop()  # 현재 입력값보다 크면 다 제거(크기 순서대로 정렬됨)
    while q and q[0][1] <= i - L: q.popleft()  # 제한 범위보다 밖이면 다 제거(일정 범위(L)보다 작거나 같아짐)
    q.append((v, i))
    D[i] = q[0][0]

print(*D)
