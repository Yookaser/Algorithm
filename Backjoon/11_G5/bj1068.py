# 1068. 트리

N = int(input())
p = list(map(int, input().split()))
d = int(input())
q = [d]

while q:  # bfs의 구조
    n = q.pop()  # 순서가 큰 상관이 없으므로 일반 리스트로 선언

    for i in range(N):
        if n == p[i]:  # 부모가 n인 경우
            q.append(i)
    p[n] = -2  # 식별하기 위해 -2로 변경

ans = 0
for i in range(N):
    if p[i] != -2 and i not in p:  # -2(삭제된 값)이 아니고 자식이 없는 경우
        ans += 1
print(ans)
