# 15650. N과 M (2)

# 방법1. 백트래킹
def dfs(depth):
    if depth == M:
        return print(*result[1:]) # 인덱스0은 0이므로 제외하고 출력
    elif M == N:
        return print(*arr) # 리스트 언팩 후 출력
    else:
        for i in arr[max(result):]: # result의 최대값은 포함되면 안됨
            result.append(i) # i추가
            dfs(depth+1) # 재귀 시행
            result.remove(i) # 재귀 끝난 뒤에는 제거해야 함(pop이 조금 더 빠름)

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
result = [0] # max함수를 위해 

dfs(0)

# 방법2. 모듈
# from itertools import combinations

# N, M = map(int, input().split())
# arr = [i for i in range(1, N+1)]

# for i in combinations(arr, M):
#     for j in range(len(i)):
#         print(i[j], end=' ')
#     print()