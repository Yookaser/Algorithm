# 2225. 합분해

N, K = map(int, input().split())
DP = [[0] * (201) for _ in range(201)]  # 행: 합에 들어간 숫자 개수, 열: 합계

for i in range(201):
    DP[1][i] = 1  # K가 1이면 무조건 1
    DP[2][i] = i + 1  # K가 2이면 i + 1

for i in range(2, 201):
    DP[i][1] = i  # N이 1일 때 i개가 나옴
    for j in range(2, 201):
        DP[i][j] = (DP[i][j-1] + DP[i-1][j]) % 1_000_000_000

print(DP[K][N])
