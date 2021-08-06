# 16953. A->B

def dfs(num, cnt):
    if num == B: # 답을 찾은 경우
        result.append(cnt) # result에 추가
        return
    elif num > B: # 값이 더 커진 경우
        return # 아무것도 안하고 return(여기서 result.append 하면 안됨)
    else:
        visited.add(num) # 방문했던 숫자 기록
        next1 = num*2 # 계산1(미리 지정해서 계산 2번 안하게 만들기)
        nuex2 = int(str(num)+'1') # 계산2

        if next1 not in visited: # 계산1 결과가 방문한 적 없는 경우
            dfs(next1, cnt+1)
        if nuex2 not in visited: # 계산2 결과가 방문한 적 없는 경우
            dfs(nuex2, cnt+1)

A, B = map(int, input().split())
visited = set() # 중복을 막기 위한 집합(in을 사용하고자 하는 것이므로 집합 자료형 사용)
result = [-1] # 답이 없는 경우를 디폴트로 설정

dfs(A, 1) # 시작 숫자, 카운트
if len(result) == 1: # 답이 없는 경우(디폴트가 1개 있으므로)
    print(-1)
else: # 답이 있는 경우
    print(min(result[1:])) # 1~리스트 길이 중 최소 출력(디폴트 -1은 제외하고)