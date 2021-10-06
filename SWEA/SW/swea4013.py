# 4013. 특이한 자석

ans = []
T = int(input())
for tc in range(1, T+1):
    K = int(input())

    res = 0
    idx = [0] * 4  # 12시 방향 인덱스
    arr = [list(map(int, input().split())) for _ in range(4)]
    
    for _ in range(K):
        a, b = map(int, input().split())

        a -= 1  # 인덱스를 맞추기 위해 -1
        t = [0] * 4  # 인덱스를 어떤 방향으로 움직일지 결정하는 리스트
        t[a] = -b
        for i in range(a, 0, -1):  # a보다 작은 방향
            if (arr[i][(idx[i]-2)%8]) != (arr[i-1][(idx[i-1]+2)%8]):  # 다른 경우
                t[i-1] = b if (a-(i-1)) % 2 else -b  # 홀수번인지 짝수번인지에 따라 방향 다르게
            else: break  # 같으면 멈춤
        
        for i in range(a, 3):  # a보다 큰 방향
            if (arr[i][(idx[i]+2)%8]) != (arr[i+1][(idx[i+1]-2)%8]):
                t[i+1] = b if ((i+1)-a) % 2 else -b
            else: break

        for i in range(4):  # 톱니바퀴 돌리기
            if t[i]:
                idx[i] = (idx[i]+t[i]) % 8  # 미리 구해둔 t[i] 값을 돌림
        
    for i in range(4):  # 최종 결과 계산
        if arr[i][idx[i]] == 1:
            res += 2**i

    ans.append('#{0} {1}'.format(tc, res))

print(*ans, sep='\n')
