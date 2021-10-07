# 1952. 수영장

ans = []
T = int(input())
for tc in range(1, T+1):
    C = list(map(int, input().split()))
    P = list(map(int, input().split()))

    DP = [0] * 12  # 12개월
    for i in range(12):
        if i < 2:  # 1일, 1달 이용권으로 점화식
            DP[i] = min(P[i]*C[0], C[1])+DP[i-1]
        elif i < 11:  # 1일, 1달, 3달 이용권으로 점화식
            DP[i] = min(min(P[i]*C[0], C[1])+DP[i-1], DP[i-3]+C[2])
        else:  # 모든 이용권으로 점화식
            DP[i] = min(min(P[i]*C[0], C[1])+DP[i-1], DP[i-3]+C[2], C[3])

    
    ans.append('#{0} {1}'.format(tc, DP[-1]))

print(*ans, sep='\n')
