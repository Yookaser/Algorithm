# 1486. 장훈이의 높은 선반

def search(arr, i, h, res):  # 완전 탐색 함수
    if i >= len(arr):  # base case
        res.append(h)
        return
    
    search(arr, i+1, h, res)
    search(arr, i+1, h+arr[i], res)


def binary_search(s, e, h):  # 이진탐색 함수
    while e > s:
        m = (s+e) // 2
        if b[m] < h:
            s = m + 1
        else:
            e = m
    return e


ans = []
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    A = list(map(int, input().split()))

    a, b = [], []
    search(A[:N//2], 0, 0, a)  # 냅색 알고리즘(완전탐색 필요 -> N이 큼 -> 반으로 나눠서 완전탐색)
    search(A[N//2:], 0, 0, b)
    b.sort()

    res = 10**6
    for i in a:  # a를 기준으로 반복
        if i + b[-1] < B: continue
        res = min(res, i+b[binary_search(0, len(b), B-i)])  # start, end, 비교값
    ans.append('#{} {}'.format(tc, res-B))

print(*ans, sep='\n')
