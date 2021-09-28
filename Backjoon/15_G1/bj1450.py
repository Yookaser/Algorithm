# 1450. 냅색문제

def search(arr, i, w, ans):  # 완전 탐색 함수
    if w > C: return  # 가지치기
    if i >= len(arr):  # base case
        ans.append(w)
        return
    
    search(arr, i+1, w, ans)  # 현재 인덱스에서 가방에 추가 X
    search(arr, i+1, w+arr[i], ans)  # 현재 인덱스에서 가방에 추가 O


def binary_search(s, e, w):  # 이진탐색 함수
    while e > s:
        m = (s+e) // 2
        if b[m] <= w:
            s = m + 1
        else:
            e = m
    return e
    # 이진탐색은 a[i]에 b 요소를 합했을 때, C보다 작거나 같은 개수를 찾아내기 위함
    # 여기서 res가 아닌 e를 반환해준 것은 결국 개수를 찾아야 하기 때문
    # (이진탐색은 결국 부등호에 따라 s와 e가 0 or 1 차이가 나게 되는데 이 점을 이용한 것)
    # 인덱스 번호를 반환하게 되면, 원래 경우의 수보다 1 작은 값이 반환되기 때문에 e를 반환함


N, C = map(int, input().split())
arr = list(map(int, input().split()))

a, b = [], []
search(arr[:N//2], 0, 0, a)  # 냅색 알고리즘(완전탐색 필요 -> N이 큼 -> 반으로 나눠서 완전탐색)
search(arr[N//2:], 0, 0, b)
b.sort()  # 이진탐색을 해야하므로 정렬

ans = 0
for i in a:  # a를 기준으로 반복
    ans += binary_search(0, len(b), C-i)  # start, end, 비교값

print(ans)
