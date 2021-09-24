# 1806. 부분합

N, S = map(int, input().split())
A = list(map(int, input().split()))

s, e = 0, 0  # 투 포인터
ans, cur = 2*N, A[0]
while 1:
    if cur < S:  # 작은 경우(e 포인터를 늘림)
        e += 1
        if e == N: break  # 종료 조건
        cur += A[e]
    elif cur >= S:  # 크거나 같은 경우(s 포인터를 늘림 & 최솟값이면 갱신)
        if ans > (e-s+1):
            ans = e - s + 1
        cur -= A[s]
        s += 1

print(ans) if ans != 2*N else print(0)  # 갱신된 경우 안된 경우에 따라 출력
