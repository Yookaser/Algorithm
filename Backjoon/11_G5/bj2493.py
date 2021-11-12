# 2493. 탑

from collections import deque


N = int(input())
A = tuple(map(int, input().split()))

q = deque([(A[-1], N-1)])  # 초기값 미리 넣어두기
ans = [0] * (N)  # 0으로 미리 선언하면 q에 남아있어도 상관 없어짐

for i in range(N-2, -1, -1):  # 오른쪽부터 진행
    while q and q[0][0] <= A[i]:
        ans[q[0][1]] = i + 1
        q.popleft()
    q.appendleft((A[i], i))  # 왼쪽에 추가(이미 while에서 자신보다 작은 수는 다 내보냄)

print(*ans)
