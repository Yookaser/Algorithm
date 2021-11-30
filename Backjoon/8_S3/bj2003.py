# 2003. 수들의 합 2

from sys import stdin


input = stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0 
for i in range(N):
    t = 0 
    for j in range(i, N):
        t += arr[j]
        if t == M:
            cnt += 1
            break
        elif t > M:
            break

print(cnt)
