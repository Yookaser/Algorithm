# 1220. Magnetic

for test in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for col in zip(*arr):
        check = False
        for x in col:
            if x == 1: check = True  # N극이면 check 활성화
            elif x == 2 and check:  # S극을 만났는데 check가 활성화가 되어있으면
                ans += 1
                check = False  # 다시 비활성화

    print('#{} {}'.format(test, ans))
