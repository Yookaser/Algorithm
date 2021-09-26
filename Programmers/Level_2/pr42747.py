# 42747. H-Index

def solution(citations):
    arr = sorted(citations)
    ans, s, e = 0, 0, len(arr)

    while e >= s:
        m = (e+s) // 2
        for i in range(len(arr)):  # 논문 탐색
            if m <= arr[i]:  # 정렬된 논문에서 처음으로 작거나 같은 경우 stop
                break
        else:  # 만약 작거나 같은 경우가 없는 경우
            e = m - 1  # e 포인터를 작게 만듬
            continue
        if len(arr) - i >= m:
            ans = m
            s = m + 1
        else:
            e = m - 1
    return ans
