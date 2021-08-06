# 15666. N과 M (12)

def dfs(depth, next):
    if depth == M:
        if tuple(result) not in visited_set: # set or dict(key)는 변경 불가능하므로 튜플로 변환해서 확인
            visited_set.add(tuple(result)) # 없는 경우이므로 방문 체크하기
            return print(*result)
        return
    for i in range(next, N): # next는 배열에서 시작할 지점(중복 가능하게 만들면서 자신보다 크거나 같은 수만 선택하게 만듬)
        result[depth] = arr[i]
        dfs(depth+1, i) # next는 idx를 넣어서 재귀에서 해당 인덱스부터 시작하게 만듬

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split()))) # 정렬하기
visited_set = set() # 이미 print한 리스트인지 점검할 집합(핵심은 in 요소이므로 집합을 사용 // dict도 가능)
result = [0] * M # 결과를 저장할 리스트(미리 인덱스 초기화하는 것이 append보다 빠름)

dfs(0, 0)