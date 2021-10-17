# 2193. 이친수

N = int(input())
DP = [0, 1, 1] + [0] * (N-2)
for i in range(3, N+1):
    DP[i] = DP[i-2] + DP[i-1]  # 점화식
print (DP[N])