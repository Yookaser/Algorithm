# 87390. n^2배열 자르기

def solution(n, left, right):
    res = []
    for i in range(left, right+1):  # 규칙을 적용
        res.append(max(i%n+1, i//n+1))
    return res
