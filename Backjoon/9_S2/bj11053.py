# 11053. 가장 긴 증가하는 부분 수열

def binary_search(l, r, x):  # 이진 탐색(x의 위치를 찾는 것)
    while r >= l:
        m = (l+r) // 2
        if v[m] >= x:
            r = m - 1
        else:
            l = m + 1
    return l  # 자신보다 작은 숫자 바로 뒤에 위치하기 위함(아래 tc 확인)


N = int(input())
arr = list(map(int, input().split()))

v = [arr[0]]
for i in range(N):
    if v[-1] < arr[i]:  # v의 최댓값보다 더 큰 경우
        v.append(arr[i])
    else:  # v의 최댓값보다 작으면 위치 찾아줌
        v[binary_search(0, len(v)-1, arr[i])] = arr[i]

print(len(v))

"""
12
10 20 20 10 30 10 40 10 50 60 0 5
==> [0, 5, 30, 40, 50, 60]
"""
