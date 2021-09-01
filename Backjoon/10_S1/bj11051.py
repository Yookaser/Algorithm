# 11051. 이항 계수 2

def combination():
    ans = 1
    for i in range(K):  # 분모 (N-K)!, 분자 K! 구현(바로 곱하고 나눔)
        ans *= (N-i)
        ans //= (i+1)
    return ans % 10007


N, K = map(int, input().split())
if K > N//2:  # K가 (N//2) 보다 크면 계산량을 줄이기 위해 (N-K)로 바꿔줌
    K = N - K

print(combination())
