# 2407. 조합

def combination(n, m):
    if m >= n//2:
        m = n - m
    
    more = deno = 1 # 초기값 1(곱해야 하므로)

    for i in range(1, m+1):
        more *= i # 1~m까지 곱함
    
    for i in range(n, n-m, -1):
        deno *= i # n-m~n까지 곱함
    
    return deno // more

N, M = map(int, input().split())
print(combination(N, M))