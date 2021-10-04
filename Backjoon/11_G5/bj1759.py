# 1759. 암호 만들기

# 방법1. combination 모듈 이용
from itertools import combinations


def isin(w):  # 검증 함수(모음 포함 여부, 자음 2개 이상 여부)
    c = 0
    for i in w:
        if i in 'aeiou':
            c += 1

    return c > 0 and len(w) - c > 1


L, C = map(int, input().split())
A = sorted(list(input().split()))  # 정렬 후 입력 받음

for comb in combinations(A, L):  # L개 조합
    t = ''.join(comb)
    if isin(t):
        print(t)


# 방법2. 비트 마스크 이용(느림)
# def isin(w):  # 검증 함수(모음 포함 여부, 자음 2개 이상 여부)
#     c = 0
#     for i in w:
#         if i in 'aeiou':
#             c += 1

#     return c > 0 and len(w) - c > 1


# def combination(arr):  # 조합 구하는 함수(비트 마스크)
#     res = []
#     for i in range((1<<len(arr))):
#         t = ''
#         for j in range(len(arr)):
#             if i & (1<<j):
#                 t += (arr[j])
#         if len(t) == L and isin(t):
#             res.append(t)
#     return res


# L, C = map(int, input().split())
# A = sorted(list(input().split()))

# print(*sorted(combination(A)), sep='\n')  # 정렬 후 출력(combinations에서 순서 바뀜)
