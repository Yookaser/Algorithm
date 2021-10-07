# 12738. 가장 긴 증가하는 부분 수열 3

# 방법1. 이진 탐색을 구현(느림)
def binary_search(l, r, x):  # 이진 탐색(x의 위치를 찾는 것)
    while r >= l:
        m = (l+r) // 2
        if B[m] >= x:
            r = m - 1
        else:
            l = m + 1
    return l  # 자신보다 작은 숫자 바로 뒤에 위치하기 위함(아래 tc 확인)


N = int(input())
A = list(map(int, input().split()))

B = [A[0]]
for i in range(1, N):
    if B[-1] < A[i]:  # B의 최댓값보다 더 큰 경우
        B.append(A[i])
    else:  # v의 최댓값보다 작으면 위치 찾아줌
        B[binary_search(0, len(B)-1, A[i])] = A[i]

print(len(B))

# 방법2. 이진 탐색 모듈 사용
# from bisect import bisect_left


# N = int(input())
# A = list(map(int, input().split()))

# B = [A[0]]
# for i in range(1, N):
#     if B[-1] < A[i]:  # B의 최댓값보다 더 큰 경우
#         B.append(A[i])
#     else:  # v의 최댓값보다 작으면 위치 찾아줌
#         B[bisect_left(B, A[i])] = A[i]

# print(len(B))