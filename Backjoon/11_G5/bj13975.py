# 13975. 파일 합치기 3

from sys import stdin
from heapq import heappush, heappop


input = stdin.readline
T = int(input())
for _ in range(T):
    K = int(input())
    A = sorted(map(int, input().split()))  # 미리 정렬하면 push 더 빠름
    q = []

    for n in A:  # heap에 push
        heappush(q, n)
    
    ans = 0
    while len(q) > 1:
        t = heappop(q) + heappop(q)  # 가장 작은 값 2개를 pop한 뒤 더함
        ans += t  # 최종 결과에 +
        heappush(q, t)  # 더한 값 다시 push
    print(ans)
