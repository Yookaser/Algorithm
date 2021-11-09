# 2217. 로프

from sys import stdin

 
input = stdin.readline
N = int(input())

arr = sorted([int(input()) for _ in range(N)], reverse=True)  # 역순 정렬

ans = 0
for i in range(N):
    if ans < arr[i] * (i+1):  # 더 큰값인 경우: 갱신
        ans = arr[i] * (i+1)
 
print(ans)
