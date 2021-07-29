# 1059. 좋은 구간

def good_range(arr, n):
    if n in arr: # 포함된 경우
        return 0
    elif n < min(arr): # 집합 S의 최솟값보다 작은 경우
        return n * (min(arr) - n) - 1 # -1을 해줘야 함
    else: # 집합 S의 원소 사이에 있는 경우
        arr.append(n) 
        arr.sort()
        state = arr.index(n) # 정렬된 집합 S에서 n의 인덱스를 찾음
        return (n - arr[state-1]) * (arr[state + 1] - n) - 1 # -1 해줘야 함

L = int(input())
set_S = list(map(int, input().split()))
n = int(input())

print(good_range(set_S, n))