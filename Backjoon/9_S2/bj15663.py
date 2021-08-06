# 15663. N과 M (9)

def dfs(depth):
    if depth == M:
        if tuple(result) not in visited_set: # set or dict(key)는 변경 불가능하므로 튜플로 변환해서 확인
            visited_set.add(tuple(result)) # 없는 경우이므로 방문 체크하기
            return print(*result)
        return
    for i in range(N):
        if visited[i]: # 방문했었는지 체크(방문 안했어야 함)
            continue
        visited[i] = 1 # 방문한 것으로 변환
        result[depth] = arr[i]
        dfs(depth+1)
        visited[i] = 0 # 방문 안 한 것으로 변환

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split()))) # 정렬하기
visited = [0] * N # 방문했는지 점검(요소의 중복이 안 되므로 사용)
visited_set = set() # 이미 print한 리스트인지 점검할 집합(핵심은 in 요소이므로 집합을 사용 // dict도 가능)
result = [0] * M # 결과를 저장할 리스트(미리 인덱스 초기화하는 것이 append보다 빠름)

dfs(0)