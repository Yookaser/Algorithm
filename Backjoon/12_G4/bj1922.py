# 1922. 네트워크 연결

from sys import stdin


def find(x):  # 자신의 집단의 루트를 찾는 함수
    if p[x] < 0: return x
    p[x] = find(p[x])
    return p[x]


def union(x, y):  # 두 집단을 합치는 함수
    x, y = find(x), find(y)

    if x != y:  # 같은 경우는 합치지 않음
        if p[x] <= p[y]:
            p[x] += p[y]
            p[y] = x
        else:
            p[y] += p[x]
            p[x] = y
        return True
    return False


input = stdin.readline
N, M = int(input()), int(input())

e = []  # edges
for _ in range(M):
    a, b, c = map(int, input().split())
    e.append((a, b, c))

e.sort(key=lambda x: x[2])  # 비용을 기준으로 정렬
p = [-1] * (N+1)  # 각 노드의 루트를 가리킴(처음에는 모두 루트)
ans = cnt = 0

for a, b, c in e:
    if union(a, b):  # a, b가 다른 집단인 경우
        ans += c
        cnt += 1
        if cnt == (N-1):  # (노드-1)개가 되면 모두 연결된 것
            print(ans)
            break
