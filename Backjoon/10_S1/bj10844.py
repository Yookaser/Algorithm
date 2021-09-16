# 10844. 쉬운 계단 수

N = int(input())
DP = [(0,1,1,1,1,1,1,1,1,1)]  # N=1인 경우 나올 수 있는 수

for i in range(1,N):
    new = [0] * 10  # 바로 전 배열 앞에 써줄 수 있는 숫자를 의미
    for j in range(10):
        if j == 0:  new[j] = DP[i-1][j+1]  # 0이면 1만 나올 수 있음(바로 전 배열의 1 인덱스의 경우의 수를 가져옴)
        elif j == 9:  new[9] = DP[i-1][j-1]  # 9인 경우는 8만 나올 수 있음
        else:  new[j] = DP[i-1][j-1] + DP[i-1][j+1]  # 1~8은 각각 2개의 수가 나올 수 있음
    DP.extend([new])

print(sum(DP[N-1]) % 1000000000)
