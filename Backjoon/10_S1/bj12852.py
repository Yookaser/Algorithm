# 12852. 1로 만들기

from collections import deque


def bfs():
    DP = [0] * (N+1)
    q = deque([N])

    while q:
        n = q.popleft()

        if n == 1: break

        if not (n%3) and not DP[n//3]:  # 3으로 나누기
            q.append(n//3)
            DP[n//3] = n
        if not (n%2) and not DP[n//2]:  # 2로 나누기
            q.append(n//2)
            DP[n//2] = n
        if not DP[n-1]:  # 1 빼기
            q.append(n-1)
            DP[n-1] = n
    
    ans = [1]
    while ans[-1] < N:  # 경로 찾기(경로를 찾을때는 무조건 이 방식으로 해야 함)
        ans.append(DP[ans[-1]])
    
    return ans

N = int(input())
ans = bfs()
print(len(ans)-1)
print(*ans[::-1])
