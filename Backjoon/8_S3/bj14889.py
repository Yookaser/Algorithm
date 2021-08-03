# 14889. 스타트와 링크

def best_match(A_team):
    A_total = 0 # A팀의 능력 합계
    B_total = 0 # B팀의 능력 합계

    B_team = list(set(list(range(N))) - set(A_team)) # B팀의 선수 구하기(filter 이용한 것이 더 빠를 것 같음)

    for i in A_team: # A팀 능력 합계 구하기
        for j in A_team:
            if i != j: # 자기자신이 아닌 경우
                A_total += team_map[i][j]
    
    for i in B_team: # B팀 능력 합계 구하기
        for j in B_team:
            if i != j: # 자기자신이 아닌 경우
                B_total += team_map[i][j]
    
    return abs(A_total - B_total) # 팀 능력치 차이의 절대값 반환


def dfs(idx, team):
    global best_score # 계속 변경해야 하는 값이므로 전역 변수 선언
    if idx == N//2: # idx가 N의 절반이 된 경우(한 팀만 구하면 되므로)
        value = best_match(team) # best_match 함수는 어차피 실행되어야 하므로 2번 시행 안되게 미리 값 받기
        if best_score > value: # 최적값보다 더 작은 경우
            best_score = value # 해당 값을 최적값으로 저장
            return # 불필요한 추가 연산이 안되도록 종료 시킴
    
    for i in range(max(team) + 1, N): # 범위 중 max(team) + 1 중요(해당 팀의 중복 선수 방지, 중복 팀 방지)
       team.append(i) # 팀에 i선수 추가
       dfs(idx+1, team) # 다음 dfs 진행(백트래킹)
       team.remove(i) # dfs 다 돌고오면, i선수 제외(아니면 계속 선수 누적됨)

import sys

input = sys.stdin.readline
N = int(input())
star_team = [0] # start팀 지정(0을 포함한 것은 미리 포함되어 있어도 결과에 상관 없고, 시간 단축시킬 수 있기 때문)
team_map = [[] for _ in range(N)] # team_map 초기화
best_score = sys.maxsize # 결과값 최대값으로 초기화

for i in range(N):
    team_map[i] = list(map(int, input().split()))

dfs(1, star_team)
print(best_score)