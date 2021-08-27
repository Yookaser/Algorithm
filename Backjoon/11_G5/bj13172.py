# 13172. Σ

import sys


def solve(A, B):
    if B == 1: return A  # B(지수)값이 1인 경우 A를 반환
    else:
        x = solve(A,B//2)  # 분할 정복
        if B % 2 == 0: return x * x % mod  # B(지수)가 짝수인 경우
        else: return x * x * A % mod  # B(지수)가 홀수인 경우


input = sys.stdin.readline
M = int(input())
ans, mod = 0, 1_000_000_007  # 결과, 나눠줄 소수
for _ in range(M):
    N, S = map(int, input().split())
    
    ans += (solve(N, mod-2)*S) % mod  # ((N의 mod-2승) * S) % mod
    ans %= mod  # 합이 mod보다 커질 수 있으므로 나머지 구해줌

print(ans)
