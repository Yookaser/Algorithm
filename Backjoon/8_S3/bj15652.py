# 15652. N과 M (4)

# 방법1. 백트래킹
def dfs(depth, next):
    if depth == M:
        return print(*result)
    else:
        for i in arr[next:]:
            result.append(i) # i추가
            dfs(depth+1, i-1) # 재귀(시작점은 -1 => 인덱스와 값의 차이가 있으므로)
            result.remove(i)  # 재귀 끝난 뒤에는 제거해야 함(pop이 조금 더 빠름)

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
result = []

dfs(0, 0) # 현재 깊이, 시작점