T = int(input())
for i in range(T):
    N = int(input())
    mylist = list(map(int, input().split(' ')))[::-1]  # 뒤에서부터 탐색
    answer = 0
    now_max = mylist[0]  # 현재 가장 큰 값

    for j in range(1, N):
        if now_max > mylist[j]:
            answer += now_max - mylist[j]
        else:
            now_max = mylist[j]

    print('#{} {}'.format(i+1, answer))