# 14003. 가장 긴 증가하는 부분 수열 5

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

B, L, res = [A[0]], [1], []  # 순서대로 증가 수열, 길이, 결과 리스트
for i in range(1, N):
    if B[-1] < A[i]:  # B의 최댓값보다 더 큰 경우
        B.append(A[i])
        L.append(len(B))  # 길이를 저장
    else:  # v의 최댓값보다 작으면 위치 찾아줌
        v = binary_search(0, len(B)-1, A[i])
        B[v] = A[i]  # v위치를 교환
        L.append(v+1)  # v의 길이 +1 저장(현재 A[i]의 값의 증가 수열의 길이임)

m = max(L)  # 최장 길이
for i in range(N-1, -1, -1):  # 가장 긴 수열을 찾는 반복(역순으로)
    if m == L[i]:  # 증가 수열의 길이와 같은 경우
        res.append(A[i])
        m -= 1
    
    if m == 0: break

print(len(res))
print(*res[::-1])  # 역순이므로 다시 역순을 취함

# 방법2. 이진 탐색 모듈 사용
# from bisect import bisect_left


# B, L, res = [A[0]], [1], []  # 순서대로 증가 수열, 길이, 결과 리스트
# for i in range(1, N):
#     if B[-1] < A[i]:  # B의 최댓값보다 더 큰 경우
#         B.append(A[i])
#         L.append(len(B))  # 길이를 저장
#     else:  # v의 최댓값보다 작으면 위치 찾아줌
#         v = bisect_left(B, A[i])
#         B[v] = A[i]  # v위치를 교환
#         L.append(v+1)  # v의 길이 +1 저장(현재 A[i]의 값의 증가 수열의 길이임)

# m = max(L)  # 최장 길이
# for i in range(N-1, -1, -1):  # 가장 긴 수열을 찾는 반복(역순으로)
#     if m == L[i]:  # 증가 수열의 길이와 같은 경우
#         res.append(A[i])
#         m -= 1
    
#     if m == 0: break

# print(len(res))
# print(*res[::-1])  # 역순이므로 다시 역순을 취함
