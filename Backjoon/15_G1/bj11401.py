# 11401 이항 계수 3

# 페르마의 소정리 (https://johngrib.github.io/wiki/Fermat-s-little-theorem/)
# 참고 (https://www.acmicpc.net/board/view/15795)
def solve(A, B):
    if B == 1: return A % p
    else:
        x = solve(A, B//2)
        if B % 2 == 0: return x * x % p
        else: return x * x * A % p


def combination(N, K):
    a, b = 1, 1  # 곱해져야 하므로 1로 초기화
    
    for i in range(N-K+1, N+1):
        a *= i
        a %= p
    for j in range(1, K+1):
        b *= j
        b %= p
        
    b = solve(b, p-2)
    return a*b % p

N, K = map(int, input().split())
p = 1000000007

print(combination(N, K))