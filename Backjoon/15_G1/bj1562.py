# 1562. 계단 수

N = int(input())
DP = [[0]*1024 for _ in range(10)]  # DP[x][y]의 형태(x는 0~9의 숫자, y는 비트 연산 값)

for i in range(1, 10):  # 초기 시작 값(1~9)을 1로
    DP[i][1<<i] = 1

for i in range(1,N):
    new = [[0]*1024 for _ in range(10)]
    for j in range(10):  # 0~9 반복
        for k in range(1024):  # 비트 연산 값 반복
            if j == 0: new[j][k|(1<<0)] += DP[j+1][k]  # 0인 경우 1 큰 수
            elif j == 9: new[j][k|(1<<9)] += DP[j-1][k]  # 9인 경우 1 작은 수
            else: new[j][k|(1<<j)] += DP[j-1][k] + DP[j+1][k]  # 1~8인 경우 양쪽
    DP = new

print(sum([DP[i][1023] for i in range(10)]) % 1000000000)  # x가 0~9까지에서 1023번째(즉, 10개의 숫자가 다 나온)의 합
