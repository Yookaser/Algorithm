# 2068. 최대수 구하기

T = int(input())

def max_value(arr):
    maximum = arr[0]

    for i in arr:
        if i > maximum:
            maximum = i
    return maximum

for _ in range(T):
    arr = list(map(int, input().split()))
    print(f'#{_ + 1} {max_value(arr)}')