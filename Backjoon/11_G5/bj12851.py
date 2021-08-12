# 12851. 숨바꼭질 2

def bfs(start_num, find_num):
    visited = deque([start_num])
    DP[start_num][1] = 1 # 자기 자신으로 오는 값을 1로 지정해줘야 함

    while visited:
        value = visited.popleft()
        
        if value == find_num:
            return DP[find_num]

        for i in [value-1, value+1, value*2]: # 갈 수 있는 node
            if i in range(len(DP)):
                if DP[i][0] == 0: # 값이 없는 경우(처음)
                    DP[i][0] = DP[value][0] + 1
                    DP[i][1] = DP[value][1] # 처음인 경우 갈 수 있는 값은 전 노드의 값(Line5를 한 이유)
                    visited.append(i) # 처음인 경우만 visted에 추가함
                elif DP[i][0] == DP[value][0] + 1: # 처음이 아닌 경우는 원래 값과 같은지 물어봐야 함
                    DP[i][1] += DP[value][1]


from collections import deque

N, K = map(int, input().split())
DP = [[0, 0] for _ in range(100001)]

result = bfs(N, K)
print(result[0])
print(result[1])