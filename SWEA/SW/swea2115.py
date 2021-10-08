# 2115. 벌꿀 채취

def adjust(arr1, arr2):  # C보다 큰 경우 조정하는 함수
    res = [0, 0]  # A 합계, B 합계
    for i in range((1<<len(arr1))):
        at, bt = 0, 0
        for j in range(len(arr1)):
            if i & (1<<j):
                at += arr1[j]
                bt += arr2[j]

        if at <= C and res[1] < bt:  # C를 만족하고 제곱합이 더 큰 경우
            res = [at, bt]
    return res


ans = []
T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int ,input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [[A[i][j]**2 for j in range(N)] for i in range(N)]

    DP_A, DP_B = [[0]*(N-M+1) for _ in range(N)], [[0]*(N-M+1) for _ in range(N)]  # 각각 A, B 합계를 저장

    for i in range(N):
        for j in range(N-M+1):
            asum = sum(A[i][j:j+M])
            if asum > C: asum, bsum = adjust(A[i][j:j+M], B[i][j:j+M])  # C를 만족하지 않는 경우 조정
            else: bsum = sum(B[i][j:j+M])  # C를 만족하면 B 합계를 계산
            DP_A[i][j] = asum
            DP_B[i][j] = bsum

    res, l = 0, len(DP_A[0])
    for i in range(l*N):
        ir, ic = divmod(i, l)
        for j in range(i, l*N):
            jr, jc = divmod(j, l)
            if ir == jr:  # 같은 행인 경우
                if jc >= ic + M:  # M 이상 차이나는 경우
                    res = max(res, DP_B[ir][ic] + DP_B[jr][jc])  # 최대값 갱신
            else:  # 다른 행인 경우
                res = max(res, DP_B[ir][ic] + DP_B[jr][jc])  # 최대값 갱신

    ans.append('#{0} {1}'.format(tc, res))

print(*ans, sep='\n')
