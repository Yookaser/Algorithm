# 2029. 몫과 나머지 출력하기

T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()))
    print(f'#{_ + 1} {arr[0] // arr[1]} {arr[0] % arr[1]}')