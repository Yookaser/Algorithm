# 소풍 (https://algospot.com/judge/problem/read/PICNIC)

def makepair(idx, team):
    global result
    if len(team) == N:  # team이 친구 수만큼 됐을 때 base case
        result += 1
        return
    
    for i in range(idx, N):  # 인원 수만큼 반복
        if i not in team:  # 해당 인원이 team에 없어야 함
            team.append(i)
            for pair in friend[i]:  # 해당 인원의 친구 반복
                if pair not in team:  # 해당 인원의 친구가 team에 없어야 함
                    team.append(pair)
                    makepair(i+1, team)
                    team.pop()  # 재귀 돌고 나왔으므로 다른 경우의 수를 위해 해당 인원의 친구 pop
            team.pop()  # 마찬가지로 재귀를 돌고 나온 것이므로 다른 경우의 수를 위해 해당 인원 pop

C = int(input())
for _ in range(C):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    friend = [[] for _ in range(N)]
    result = 0

    for i in range(M):  # 인접리스트 생성
        friend[arr[i*2]].append(arr[i*2+1])

    makepair(0, [])
    print(result)
