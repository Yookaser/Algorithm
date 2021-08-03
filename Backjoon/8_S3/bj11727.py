# 11727. 2*n 타일링 2

def tiling(num):
    if num <= 1: # 2보다 작으면 이미 지정되어 있고 자기 자신이므로 num 반환
        return num
    
    for i in range(2, num+1): # 범위는 2부터 num까지
        if i % 2 == 0: # 짝수인 경우
            DP[i] = (DP[i-1]*2) + 1 # 점화식(다른 점화식은 'DP[i] = DP[i-1] + DP[i-2]*2' 도 있음 홀짝 관계 없이)
        else: # 홀수인 경우
            DP[i] = (DP[i-1]*2) - 1 # 점화식

    return DP[num] % 10007 # 문제 조건 10007 나머지 반환하는 것 빼먹지 말기

N = int(input())
DP = [0] * 1001 # 점화식 세우기(0번 인덱스는 헷갈리지 않기 위해 만듬)
DP[1] = 1 # 1은 점화식상 필요하므로 해당 값 미리 지정

print(tiling(N))