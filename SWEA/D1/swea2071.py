# 2071. 평균값 구하기

T = int(input())

def mean_list(arr):
    total = 0
    for i in arr:
        total += i
    return round(total/len(arr))

for _ in range(T):
    arr = list(map(int, input().split()))
    print(f'#{_ + 1} {mean_list(arr)}')