# 11726. 2*n 타일링

def tiling(num):
    if num <= 2: # 2보다 작으면 이미 지정되어 있고 자기 자신이므로 num 반환
        return num
    for i in range(3, num+1): # 범위는 3부터 num까지
        DP[i] = DP[i-1] + DP[i-2] # 점화식

    return DP[num] % 10007 # 문제 조건 10007 나머지 반환하는 것 빼먹지 말기

N = int(input())
DP = [0] * 1001 # 점화식 세우기(0번 인덱스는 헷갈리지 않기 위해 만듬)
DP[1], DP[2] = 1, 2 # 1, 2는 점화식상 필요하므로 해당 값 미리 지정

print(tiling(N))