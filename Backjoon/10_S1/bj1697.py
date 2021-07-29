# 1697. 숨바꼭질

# 방법1. DP(시간 140)
N, K = list(map(int, input().split()))

if N >= K: # K가 작으면 -1씩 이동할 수 밖에 없음(같다면 0)
    print(N - K)
else:
    DP = list(reversed(range(0, N+1))) + [100001] * (K - N) # [0~N](N+1개) + [100001](N-K개) => 총 K+1개
    
    for i in range(N+1, K+1): # N부터 들어가면 line15에서 i-1 오류 발생할 수 있음(N=0일때)
        if i % 2 == 0: # 짝수인 경우
            DP[i] = min(DP[i-1] + 1, DP[i//2] + 1) # (바로 앞의 값 + 1 OR 2나눈 값 + 1) 중 작은 값
        else: # 홀수인 경우
            DP[i] = min(DP[i-1] + 1, DP[(i+1)//2] + 2) # (바로 앞의 값 + 1 OR 바로 뒤의 값을 2로 나눈 값 + 2) 중 작은 값
    
    print(DP[K])

# 방법2. BFS(시간 284ms) => N 이하의 값을 미리 안정해서 2배의 차이가 나는 것 같음
# def BFS(start_num, find_num): # 인자 안받아도 되긴 함(전역변수 참조해서)
#     visited_list = deque([start_num]) # 방문했던 요소들이 잠시 거쳐갈 곳(앞에서 POP해야 하므로 deque로)

#     while visited_list: # visited_list에 아무것도 없으면 끝
#         value = visited_list.popleft() # 맨 앞에 값 받음
        
#         if value == find_num: # value가 찾는 값이랑 같은 경우
#             return DP[find_num] # 해당 DP 값 반환
        
#         for i in [value-1, value+1, value*2]: # 바로 앞의 값, 바로 뒤의 값, 2배한 값 반복
#             if i in range(0, len(DP)) and DP[i] == 0: # 단, 범위는 DP 리스트 안에 있는 경우
#                 DP[i] = DP[value] + 1 # i는 해당 value에서 +1 값(첫 value는 start_num(N))
#                 visited_list += [i] # 여기에 추가하고 그 순서대로 leftpop으로 받아서 반복함


# from collections import deque

# N, K = list(map(int, input().split()))
# DP = [0] * 100001 # 0으로 지정(만약 0이 아닌 경우 line30 에서 조건식을 바꿔야 하고, 초기 DP[start_num] = 0을 설정해야 함)

# print(BFS(N, K))