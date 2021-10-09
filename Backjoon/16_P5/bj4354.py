# 4354. 문자열 제곱

# 방법1. 약수 이용
def divisor(n):
    res = [1, n]  # 1과 자기자신은 base
    for i in range(2, int(n**0.5)+1):  # 에라토스테네스의채와 같은 범위를 이용
        if not (n%i):
            res.append(i)
            if (i!=n//i): res.append(n//i)  # 나눈 몫도 추가
    return sorted(res, reverse=True)


while True:
    S = input()
    if S == '.': break

    for i in divisor(len(S)):
        if S == (S[:(len(S)//i)]*i):  # len(S)를 i로 나눈 값의 길이를 i번 곱해서 같은 값인 경우
            ans = i
            break

    print(ans)

# 방법2. KMP(매우 느림)
# def maketable(P):
#     j, res = 0, [0] * len(P)
#     for i in range(1, len(P)):
#         while j > 0 and P[i] != P[j]:  # 0이 되거나 같을때까지 이전으로 돌아가서 비교
#             j = res[j-1]
#         if P[i] == P[j]:  # 같은 경우 res를 갱신
#             j += 1
#             res[i] = j
#     return res


# while True:
#     S = input()
#     if S == '.': break

#     if len(S) == 1:  # 길이가 1이면 아래 for문에서 에러남
#         ans = 1
#     else:
#         A = maketable(S)
#         m = A[-1]
#         for i in range(len(S)-1, -1, -1):  # 역순으로 검사
#             if A[i] != m:  # 같지않다면 패턴 없는 것
#                 ans = 1
#                 break
#             m -= 1

#             if m == 0:  # 반복되는 패턴이 나온 경우
#                 if (len(S)/i) != (len(S)//i): ans = 1  # 'abcdabcdabcdabc' 케이스 고려(마지막만 패턴이 안나오는 경우)
#                 else: ans = len(S) // i  # 전체 길이 / 패턴을 뺀 남은 길이(ex - aaaa이면 i는 1일때 멈춤)
#                 break
#     print(ans)
