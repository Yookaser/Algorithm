# 2063. 중간값 찾기

N = int(input())
arr = list(map(int, input().split()))

def odd_median(arr):
    arr.sort()
    return arr[int(N//2)]

print(odd_median(arr))