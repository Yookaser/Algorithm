# 1986. 지그재그 숫자

T = int(input())
total = 0

for _ in range(T):
    N = int(input())

    if N % 2 == 1: # 홀수인 경우
        total += N
    else: # 짝수인 경우
        total -= N
    
    print(f'#{_ + 1} {total}')