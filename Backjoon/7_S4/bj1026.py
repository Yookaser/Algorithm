# 1026. 보물

from sys import stdin


N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

ans = 0
for i in range(N):
    ans += A[i] * B[i]  # 작은 순서 * 큰 순서
print(ans)
