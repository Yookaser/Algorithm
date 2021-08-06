# 15657. N과 M (8)

def dfs(depth, next):
    if depth == M:
        return print(*result)
    for idx in range(next, N): # next는 배열에서 시작할 지점(중복 가능하게 만들면서 자신보다 크거나 같은 수만 선택하게 만듬)
        result[depth] = arr[idx]
        dfs(depth+1, idx) # next는 idx를 넣어서 재귀에서 해당 인덱스부터 시작하게 만듬

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split()))) # 정렬하기
result = [0] * M # 결과를 저장할 리스트(미리 인덱스 초기화하는 것이 append보다 빠름)

dfs(0, 0)

