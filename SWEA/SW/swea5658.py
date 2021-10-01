# 5658. 보물상자 비밀번호

from collections import deque


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = deque(list(input()))

    ans = set()
    for _ in range(N):
        for i in range(0, N, N//4):
            t = '0x'  # 16진수 변환을 위해 지정
            for j in range(N//4):
                t += A[i+j]
            ans.add(int(t, 16))  # 16진수 문자열 => 10진수 변환 후 저장
        A.appendleft(A.pop())  # 회전

    print('#{0} {1}'.format(tc, sorted(list(ans), reverse=True)[K-1]))
