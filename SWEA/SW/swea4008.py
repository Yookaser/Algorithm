# 4008. 숫자 만들기

def dfs(n, a, s, m, d, v):  # 인덱스, 덧셈, 뺄셈, 곱셈, 나눗셈, 값
    global res1, res2
    if n == N:
        res1 = max(res1, v)  # 최대값
        res2 = min(res2, v)  # 최소값
        return

    if a: dfs(n+1, a-1, s, m, d, v+B[n])
    if s: dfs(n+1, a, s-1, m, d, v-B[n])
    if m: dfs(n+1, a, s, m-1, d, v*B[n])
    if d: dfs(n+1, a, s, m, d-1, int(v/B[n]))


ans = []
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A, B = list(map(int, input().split())), list(map(int, input().split()))

    res1, res2 = -100000000, 100000000  # 최대값, 최소값
    dfs(1, A[0], A[1], A[2], A[3], B[0])
    ans.append('#{0} {1}'.format(tc, res1-res2))

print(*ans, sep='\n')
