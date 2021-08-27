# 1629. 곱셈

def solve(A, B):
    if B == 1: return A % C  # B(지수)값이 1인 경우 A를 반환(A=10, B=1, C=7인 경우를 대비하기 위해 C 나머지를 리턴)
    else:
        x = solve(A,B//2)  # 분할 정복
        if B % 2 == 0: return x * x % C  # B(지수)가 짝수인 경우
        else: return x * x * A % C  # B(지수)가 홀수인 경우


A, B, C = map(int, input().split())

print(solve(A,B))