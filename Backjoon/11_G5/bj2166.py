# 2166. 다각형의 면적

from sys import stdin


input = stdin.readline
N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
A.append((A[0][0], A[0][1]))

ans = 0
for i in range(N):  # 신발끈 이론 적용
    ans += (A[i][0]*A[i+1][1]) - (A[i][1]*A[i+1][0])
print(round(abs(ans)/2, 1))
