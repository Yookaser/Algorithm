# 1062. 가르침

from sys import stdin
from itertools import combinations


input = stdin.readline
N, K = map(int, input().split())

if K < 5:  # K가 5보다 작으면 무조건 0
    [input() for _ in range(N)]  # 입력 처리
    print(0)
else:
    ans, n = 0, 0  # 최종 출력값, 카운팅 변수
    ws = []  # 비트로 변환한 문자을 저장
    base, p = set('antic'), set()  # 기본 문자 집합, 가능한 문자 집합 저장
    convert={chr(ord('a')+i):1<<i for i in range(26)}  # 이진 변환을 미리 저장(시간 단축을 위해)
    
    for i in range(N):
        w = set(list(input().rstrip())).difference(base)
        if w and len(w) <= (K-5):  # 기본 이외의 문자가 있고 길이가 (K-5)보다 작은 경우(크면 어차피 못 만듬)
            b = 0
            p |= w  # 가능한 문자에 더해주기
            for i in w:  # 이진 변환
                b += convert[i]
            ws.append(b)  # 비트로 변환한 문자 저장
        elif not w:  # w가 없는 경우(무조건 만들 수 있는 경우)
            n += 1
    
    if len(p) <= (K-5):  # 가능한 문자가 (K-5)보다 작거나 같은 경우
        print(len(ws)+n)
    else:
        for cs in combinations(p, K-5):
            b, tn = 0, 0
            for c in cs:  # 이진 변환(해당 조합에 대해서)
                b += convert[c]
            
            b ^=(1<<26) - 1  # 역 처리((2**26)-1을 의미하고, 밑의 연산을 위해)
            for w in ws:
                if not b & w:  # 겹치는 것이 없는 경우(역 처리된 b이므로 겹치는 것이 없다면 만들 수 있는 것)
                    tn += 1

            ans = max(ans, n+tn)  # 최대값 갱신
        print(ans)
