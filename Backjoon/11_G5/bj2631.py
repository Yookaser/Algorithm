# 2631. 줄세우기

from sys import stdin

input = stdin.readline
N = int(input())
A = [int(input()) for _ in range(N)]
dp = [0] * N

dp[0] = 1  # 초기값 지정
for i in range(1, N):
    a = []
    for j in range(i):
        if A[i] > A[j]: a.append(dp[j])
    if not a:
        dp[i] = 1
    else:
        dp[i] = max(a) + 1

print(N - max(dp))
