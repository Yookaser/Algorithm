# 1984. 중간 평균값 구하기

def mid_mean(arr):
    arr.sort() # 최대, 최소 값을 제외한 슬라이싱을 위해
    return round(sum(arr[1:-1]) / (len(arr) - 2)) # (최대 최소 제외 합계) / (요인 수 - 2)

T = int(input())

for _ in range(T):
    num_list = list(map(int, input().split()))
    print(f'#{_ + 1}', mid_mean(num_list))