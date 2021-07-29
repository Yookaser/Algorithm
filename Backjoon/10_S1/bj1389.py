# 1389. 케빈 베이컨의 6단계 법칙

# 방법1. 리스트
def six_rule(kevin_map):
    result = [0]
    for i in range(1, len(kevin_map)): # 1~N번 사람 반복
        kevin_number = [[] for _ in range(6)] # 2차원 리스트로 요소는 i번째에서 N번 이동하여 접근 가능한 리스트를 담을 공간
        kevin_number[1] = kevin_map[i] # 첫 번째는 kevin_map의 i번째(한 번에 이동 가능한 것)
        cnt = 1 # counting을 위한 변수

        while cnt < 5:
            for j in kevin_number[cnt]: # i번째에서 N번 이동하여 접근 가능한 리스트를 반복
                kevin_number[cnt + 1] += kevin_map[j] # kevin_map의 j번째의 값들을 kevin_number에 저장
            kevin_number[cnt + 1] = list(set(kevin_number[cnt + 1])) # 중복은 제거(중복은 for문 시간만 늘림)
            cnt += 1

        kevin_sum = 0 # 각 요소의 합을 저장하기 위한 변수

        for m in range(1, len(kevin_map)): # 1~N번 사람 반회
            for n in range(1, len(kevin_number)): # 1~5 kevin_number 반복(1~5번 이동하여 도달 가능한 요인들을 의미)
                if i == m: # 자기자신이므로 제외
                    continue
                if m in kevin_number[n]: # m번(사람)이 해당 kevin_number에 있는 경우
                    kevin_sum += n
                    break # 더 이상 n이 돌 필요가 없으므로 정지
            else: # 만약, break가 걸리지 않는 경우(즉, 사람이 6번 이내로 안 이어지는 경우!!! 이거 제일 많은 시간 소비함)
                kevin_sum += 6 # 임의의 숫자 6 더함
        result += [kevin_sum] # 함계를 최종 리스트에 저장
    return result.index(min(result[1:])) # min값 인덱스 반환

import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
kevin_map = [[] * (N + 1) for i in range(N+1)] # 인덱스 헷갈리지 않기 위해 0~N(N + 1개)로 만듬

for i in range(M):
    x, y = list(map(int, input().split()))
    kevin_map[x] += [y]
    kevin_map[y] += [x]  # 양방향이므로 반대도 해줘야 함

print(six_rule(kevin_map))

# 방법2. 집합(집합이 더 빠르게 찾을 것이라 생각했는데, 리스트보다 살짝 느림)
# def six_rule(kevin_map):
#     result = [0]
#     for i in range(1, len(kevin_map)):
#         kevin_number = [set() for _ in range(6)]
#         kevin_number[1] = kevin_map[i]
#         cnt = 1

#         while cnt < 5:
#             for j in kevin_number[cnt]:
#                 kevin_number[cnt + 1].update(kevin_map[j])
#             cnt += 1

#         kevin_sum = 0

#         for m in range(1, len(kevin_map)):
#             for n in range(1, len(kevin_number)):
#                 if i == m:
#                     continue
#                 if m in kevin_number[n]:
#                     kevin_sum += n
#                     break
#                 else:
#                     kevin_sum += 6
#         result += [kevin_sum]
#     return result.index(min(result[1:]))


# import sys

# input = sys.stdin.readline

# N, M = list(map(int, input().split()))
# kevin_map = [set() for i in range(N+1)]


# for i in range(M):
#     x, y = list(map(int, input().split()))
#     kevin_map[x].add(y)
#     kevin_map[y].add(x)

# print(six_rule(kevin_map))

# 방법3. BFS
# def BFS(num):
#     result = [0] * (N + 1) # 결과를 저장할 공간(각 사람과 관계가 몇 인지 // 미리 0으로 선언하면 자기자신은 건들 필요 X)
#     bfs_list = [num]
#     visited_list = [num]

#     while visited_list: # visit_list가 0이면 끝남
#         value = visited_list.pop(0) # 제일 처음 값의 노드 저장
#         for i in kevin_map[value]: # i는 value와 한 번에 이동 가능한 사람을 반복
#             if i not in bfs_list: # 이미 방문했던 사람에 속하지 않는 경우
#                 result[i] = result[value] + 1 # value에서 + 1을 함(즉, 자기자신과 value번째 사람의 거리에서 + 1 하는 것 -> 핵심 )
#                 bfs_list += [i] # 방문했던 리스트에 추가
#                 visited_list += [i] # 방문한 리스트에 추가(해당 리스트 다 지울때까지 돌아야 함)

#     return sum(result) # 합계를 반환

# import sys

# input = sys.stdin.readline

# N, M = list(map(int, input().split()))
# kevin_map = [[] * (N + 1) for i in range(N+1)] # 인덱스 헷갈리지 않기 위해 0~N(N + 1개)로 만듬
# result = [0]

# for i in range(M):
#     x, y = list(map(int, input().split()))
#     kevin_map[x] += [y]
#     kevin_map[y] += [x]  # 양방향이므로 반대도 해줘야 함

# for i in range(1, N + 1): # 1~N번 사람 반복
#     result += [BFS(i)] # BFS 결과(각 사람의 관계의 합계)를 저장

# print(result.index(min(result[1:]))) # min값 인덱스 반환