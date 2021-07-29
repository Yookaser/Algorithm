# 2072. 홀수만 더하기

T = int(input())

def sum_odd(arr):
    total = 0

    for i in arr:
        if i % 2 != 0:
            total += i
    return total

for _ in range(T):
    arr = list(map(int, input().split()))
    print(f'#{_ + 1} {sum_odd(arr)}')