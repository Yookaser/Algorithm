# 1204.최빈수 구하기

def mode(arr):
    counts = [0] * (101) # 각 점수(0 ~ 100)를 표현하는 공간(해당 점수가 몇 개 있는지)
    for i in arr:
        counts[i] += 1
    
    maxi = max(counts)

    if counts.count(maxi) == 1: # 최빈값의 점수가 1개인 경우
        return counts.index(maxi)
    else: # 최빈값의 점수가 2개 이상인 경우(최대값 찾기)
        rev = counts[::-1].index(maxi) # index는 앞에서 1개만 찾으므로, 역전시켜 인덱스를 찾음
        return 101 - (rev + 1) # 찾은 인덱스를 이용하여 점수로 변환


T = int(input())

for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{N} {mode(arr)}')