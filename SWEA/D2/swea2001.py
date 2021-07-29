# 2001. 파리 퇴치

def kill_fly(arr, size): # 단순한 브루트 포스 방식(더 효율적인 방법을 찾아봐야 할 듯)
    kill_list = []

    for row in range(len(arr) + 1 - size): # 가로 시작값
        for col in range(len(arr) + 1 - size): # 세로 시작값
            cnt = 0 # 합계 초기화

            for row_size in range(size): # 가로 블럭 구현
                for col_size in range(size): # 세로 블럭 구현
                    cnt += arr[row + row_size][col + col_size]
            kill_list.append(cnt)

    return max(kill_list)

T = int(input())

for _ in range(T):
    N, M = list(map(int, input().split()))
    fly_map = []
    for i in range(N):
        fly_map.append(list(map(int, input().split())))
    print(f'#{_ + 1}', kill_fly(fly_map, M))