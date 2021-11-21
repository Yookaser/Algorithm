# 5557. 1학년

from sys import stdin
input = stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = [[0] * 21 for i in range(n)]
dp[0][A[0]] = 1
for i in range(1, n - 1):
    for j in range(21):
        if dp[i - 1][j]:
            if 0 <= j + A[i] <= 20: dp[i][j + A[i]] += dp[i - 1][j]
            if 0 <= j - A[i] <= 20: dp[i][j - A[i]] += dp[i - 1][j]

print(dp[n - 2][A[-1]])
