# 17417. 게리멘더링

from collections import deque
from itertools import combinations


def bfs(a):
    n = a.pop()
    q = deque([n])
    visited = set([n])

    while q:
        n = q.popleft()

        if not a:  # 모든 노드를 순환한 경우
            return True
        
        for i in A[n]:
            if i in a and i not in visited:  # 순환 가능한 경우
                a.remove(i)
                q.append(i)
    return False  # 순환 불가능한 경우


def sub_people(a, b):  # 인구 차이 구하는 함수
    sum_a = sum([P[i] for i in a])
    sum_b = sum([P[i] for i in b])
    return abs(sum_a - sum_b)


N = int(input())
P = [0] + list(map(int, input().split()))  # 인구
A  = [0] * (N+1)  # 연결 리스트
ans = sum(P)  # 결과는 미리 최대값으로
all = [i for i in range(1, N+1)]  # 비교를 위한 리스트
visited = set()

for i in range(1, N+1):
    a = list(map(int, input().split()))
    A[i] = a[1:]


for i in range(1, N//2+1):  # 조합이므로 불필요 반복은 줄입
    for x in combinations(all, i):
        x = set(x)
        y = set(all) - x  # 전체 중 x가 아닌 것을 y에 포함

        sub = sub_people(x, y)  # 차이 구하기
        if ans > sub and bfs(x) and bfs(y):  # 갱신될 수 있고, x와 y 모두 순환 가능한 경우
            ans = sub

if ans == sum(P):  # 갱신된 적 없는 경우
    print(-1)
else:
    print(ans)

