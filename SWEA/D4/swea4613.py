# 4613. 러시아 국기 같은 깃발

def check1(c_list, w):  # 행마다 매개변수 w 문자가 아닌 개수를 저장하고 반환하는 함수
    for r in range(N):
        cnt = 0
        for c in range(M):
            if arr[r][c] != w:  # 해당 문자가 아닌 경우
                cnt += 1
        c_list.append(cnt)
    return c_list  # 결과 리스트 반환


def check2():  # 각 문자가 가질 수 있는 열 개수를 만드는 함수
    c_list = []
    for w in range(1, N-1):  # 흰
        for b in range(1, N-1):  # 파랑 
            for r in range(1, N-1):  # 빨강
                x = w+b+r
                if x == N:  # 더한 값이 총 행 수와 같은 경우 저장
                    c_list.append((w, b, r))
                elif x > N:  # 더한 값이 총 행수보다 큰 경우 정지
                    break
    return c_list  # 결과 리스트 반환


T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    cw, cb, cr = check1([], 'W'), check1([], 'B'), check1([], 'R')  # 각각의 개수를 저장
    result = check2()  # 가능한 경우의 수 저장


    print(cw)
    print(result)

    ans = 2501  # 최대 칠해야 하는 개수는 50*50이므로 +1한 값
    for i, j, k in result:
        temp = 0
        temp += sum(cw[:i])  # 흰으로 칠해야 하는 개수
        temp += sum(cb[i:i+j])  # 파랑으로 칠해야 하는 개수
        temp += sum(cr[i+j:i+j+k])  # 빨강으로 칠해야 하는 개수
        ans = min(ans, temp) # 최소값 저장

    print('#{} {}'.format(test+1, ans))
