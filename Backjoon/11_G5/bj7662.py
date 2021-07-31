# 7662. 이중 우선순위 큐

import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    min_q, max_q = [], [] # 이중 힙큐를 만들 것(최소, 최대)
    visited_list = [False] * 1000001 # 해당 인덱스를 방문했던 값인지 판별하기 위한 공간(초기는 방문 안했으므로 False / 최대 1000000의 N을 입력받으므로 1000001로 설정)
    N = int(input())

    for idx in range(N):
        command, num = input().split() # 명령, 숫자
        if command == 'I': # 입력 받는 경우
            heapq.heappush(min_q, (int(num), idx)) # 최소힙에 저장(값, idx)
            heapq.heappush(max_q, (-int(num), idx)) # 최대힙에 저장(-값, idx)
            visited_list[idx] = True # 방문했으므로 True로 변환(idx임을 주의할 것)

        elif num == '-1': # 최소값 pop인 경우(else가 아닌 elif를 쓴 것은 조금이라도 연산을 줄이기 위해 -> else면 안에 if num == '-1' 또 써야했음)
            while min_q and not visited_list[min_q[0][1]]: # 빈 큐가 아니고, 방문했던 리스트가 아닌 경우(False -> 즉, 이미 pop된 것 -> max_q에서) 반복함
                heapq.heappop(min_q) # while에 걸린다면, 계속 pop
            if min_q: # 빈 큐가 아닌 경우
                visited_list[heapq.heappop(min_q)[1]] = False # pop하므로 방문 안했던 것으로 바꿈

        else: # 최대값 pop
            while max_q and not visited_list[max_q[0][1]]: # 빈 큐가 아니고, 방문했던 리스트가 아닌 경우(False -> 즉, 이미 pop된 것 -> min_q에서) 반복함
                heapq.heappop(max_q)
            if max_q: # 빈 큐가 아닌 경우
                visited_list[heapq.heappop(max_q)[1]] = False # pop하므로 방문 안했던 것으로 바꿈

    while min_q and not visited_list[min_q[0][1]]: # 위의 while문과 똑같음(다시 해주는 이유는 for문이 끝나고, 안 맞는 경우가 있기 때문! 위에서 while은 정확한 값을 pop하기 위함)
        heapq.heappop(min_q)
    while max_q and not visited_list[max_q[0][1]]:
        heapq.heappop(max_q)

    if min_q and max_q: # 빈 큐들이 아닌 경우
        print(f'{-1 * max_q[0][0]} {min_q[0][0]}')
    else: # 빈 큐인 경우
        print('EMPTY')