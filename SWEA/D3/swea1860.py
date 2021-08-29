# 1860. 진기의 최고급 붕어빵

T = int(input())
for test in range(T):
    N, M, K = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    ans = 'Possible'

    if arr[0] == 0:  # 시작 시간에 오면 무조건 불가능
        ans = 'Impossible'
    else:
        c, idx = 0, 0  # 붕어빵 개수, 배열의 순서를 가리킴
        for i in range(1, arr[-1]+1):  # 시간은 1 ~ 마지막 손님이 오는 시간(포함)
            if (i%M) == 0:  # M의 배수가 되면 붕어빵 +K
                c += K

            while idx < N and arr[idx] <= i:  # idx가 범위 내이고, 손님이 오는 시간이 현재 시간보다 작거나 같을 때 반복
                c -= 1
                idx += 1
            
            if c < 0:  # 붕어빵 개수가 음수라면 break
                ans = 'Impossible'
                break

    print('#{} {}'.format(test+1, ans))
