# 1285. 아름이의 돌 던지기(python 미지원)

def rock(arr):
    arr = list(map(abs, arr)) # 리스트 각 인자 절대값 변환

    return min(arr), arr.count(min(arr)) # 최솟값, 해당 최솟값의 개수 반환

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    solu1, solu2 = rock(arr)

    print(f'#{_ + 1} {solu1} {solu2}')