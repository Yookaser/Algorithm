# 13711. LCS 4

def binary_search(x, l):  # 이진탐색 함수(위치를 찾을 값, 탐색 리스트 길이)
    s, e = 0, l
    while s < e:
        m = (s+e) // 2
        if ans[m] < x: s = m + 1
        else: e = m
    return e


N = int(input())
A, B = tuple(map(int, input().split())), tuple(map(int, input().split()))

b = [0] * N
for i in range(N):  # B의 인덱스(숫자-1)에 해당 숫자의 인덱스 번호를 넣음
    b[B[i]-1] = i + 1

ab = [0] * N
for i in range(N):  # A의 숫자가 b에서 어디에 있는지 저장
    ab[i] = b[A[i]-1]

ans = [ab[0]]
for i in range(1, N):  # LIS 풀이 구현
    if ab[i] > ans[-1]: ans.append(ab[i])
    else:
        ans[binary_search(ab[i], len(ans)-1)] = ab[i]

print(len(ans))

'''
10
1 5 9 3 7 4 8 6 2 10
3 2 1 6 5 4 9 8 7 10
[3, 5, 7, 1, 9, 6, 8, 4, 2, 10]
'''
