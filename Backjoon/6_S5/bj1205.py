# 1205. 등수 구하기

N, score, P = list(map(int, input().split()))
if N != 0: # 0이면 입력을 안 받는 경우가 있음(입력을 안 받는데 달라고 하면 EOFError가 발생)
    arr = list(map(int, input().split()))

same_list = []

if N == 0: # N이 0이면 무조건 1
    print(1)

else:
    arr.sort(reverse = True) # 역순으로 정렬해야 함
    for i in range(P):
        if score > arr[i]: # 반복을 돌다가 자신의 점수보다 작은 값을 만난 경우
            if score == arr[i - 1]: # 작은 값의 바로 전 값이 자신의 점수랑 같은 경우
                print(arr.index(arr[i - 1]) + 1) # 해당 (인덱스 + 1) 출력
            else: # 작은 값의 바로 전 값이 자신의 점수랑 다른 경우
                print(i + 1)
            break

        elif i == N - 1: # 자신보다 작은 값을 못 만나고, 리스트의 마지막 인자에 도달한 경우
            if P > N:
                if score == arr[i]: # 작은 값의 바로 전 값이 자신의 점수랑 같은 경우
                    print(arr.index(arr[i]) + 1) # 해당 (인덱스 + 1) 출력
                else: # 작은 값의 바로 전 값이 자신의 점수랑 다른 경우
                    print(N + 1) # (리스트 길이 + 1)
                break
            else: # p == N인 경우
                print(-1)
            break