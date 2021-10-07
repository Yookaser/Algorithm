# 3752. 가능한 시험 점수

ans = []
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    v = [0]  # 방문 리스트(0은 방문)
    DP = [1] + [0] * sum(arr)  # 인덱스: 숫자, 값: 1이면 나온 값
    for i in arr:
        for j in v[:]:  # 슬라이싱으로 해야 함(for문 내에서 값이 추가되므로)
            if DP[i+j]: continue  # 이미 나온 값은 거름
            DP[i+j] = 1  # 방문 표시
            v.append(i+j)

    ans.append('#{0} {1}'.format(tc, len(v)))

print(*ans, sep='\n')
