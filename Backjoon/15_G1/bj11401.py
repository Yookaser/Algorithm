# 11401 이항 계수 3

# 1. nCr = ((n-k)!/k!) % p
# 2. A = (n-k)!, B = k!
# 3. A * B**(-1) % p  (1 = b**(p-1))
# 4. A * B**(p-2) % p (페르마의 정리로 문제에서 p*(소수)로 나눈 나머지를 구하라고 해서 구할 수 있는 식)
def solve(A, B):
    if B == 1: return A % p  # 시작부터 B가 1인 경우를 위해 나머지 연산
    else:
        x = solve(A, B//2)  # 분할 정복
        if B % 2 == 0: return x * x % p  # 2의 배수면 x의 제곱
        else: return x * x * A % p  # 2의 배수가 아니면 +1된 값일 것이므로 x의 제곱에 A를 곱함


def combination(N, K):
    a, b = 1, 1  # 곱해져야 하므로 1로 초기화
    
    for i in range(N-K+1, N+1):  # (n-k)! 구하기
        a *= i
        a %= p
    for j in range(1, K+1):  # k! 구하기
        b *= j
        b %= p
        
    b = solve(b, p-2)  # (k!)**(p-2) 구하기
    return a*b % p  # 이항 계수값 구하기


N, K = map(int, input().split())
p = 1_000_000_007

print(combination(N, K))
