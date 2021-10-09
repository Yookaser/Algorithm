# 1768. 찾기

from sys import stdin


def maketable(P):
    j, res = 0, [0] * len(P)
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:  # 0이 되거나 같을때까지 이전으로 돌아가서 비교
            j = res[j-1]
        if P[i] == P[j]:  # 같은 경우 res를 갱신
            j += 1
            res[i] = j
    return res


def kmp(T, P, t):
    j, res = 0, []
    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:  # 0이 되거나 같을때까지 이전으로 돌아가서 비교
            j = t[j-1]
        if T[i] == P[j]:
            if j == len(P) - 1:  # T에 P가 등장한 경우
                res.append(i-len(P)+2)  # 결과에 시작 인덱스 저장
                j = t[j]  # j 갱신(0으로 돌아가면 안됨)
            else:  # 아직 등장하지 않은 경우
                j += 1
    return res


input = stdin.readline
T, P = input().rstrip(), input().rstrip()

ans = kmp(T, P, maketable(P))
print(len(ans))
print(*ans)
