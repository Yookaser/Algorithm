# 2070. 큰 놈, 작은 놈, 같은 놈

T = int(input())

def compare(num1, num2):
    if num1 > num2:
        return '>'
    elif num1 == num2:
        return '='
    elif num1 < num2:
        return '<'

for _ in range(T):
    arr = list(map(int, input().split()))
    print(f'#{_ + 1} {compare(arr[0], arr[1])}')