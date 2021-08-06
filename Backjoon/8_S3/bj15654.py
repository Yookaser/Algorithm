# 15654. N과 M (5)

def dfs(depth):
    if depth == M:
        return print(*result)
    
    for i in range(N):
        if visited[i]: # 방문했었는지 체크(방문 안했어야 함)
            continue
        visited[i] = 1 # 방문한 것으로 변환
        result[depth] = arr[i] # depth의 인덱스 값을 arr[i]의 값으로(pop할 필요는 없음 => 덮어씌워짐)
        dfs(depth+1) # 재귀
        visited[i] = 0 # 방문 안 한 것으로 변환

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split()))) # 정렬하기
visited = [0] * N # 방문했는지 점검(요소의 중복이 안 되므로 사용)
result = [0] * M # 결과를 저장할 리스트(미리 인덱스 초기화하는 것이 append보다 빠름)

dfs(0)