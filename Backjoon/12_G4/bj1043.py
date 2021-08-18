# 1043. 거짓말

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
notLie = set(map(int, input().split()[1:])) # 진실을 아는 사람 집합(첫 번째는 필요 없으므로 제외하고 받기)
arr = [set(map(int, input().split()[1:])) for _ in range(M)] # 파티(첫 번째는 필요 없으므로 제외하고 받기)

for i in range(M): # 파티 수만큼 반복(진실을 아는 사람에게 들은 사람에게 들은 사람이 ~~ 아는 경우를 고려해야 함)
    for party in arr:
        if notLie.intersection(party): # 진실을 아는 사람이 파티에 속한 경우
            notLie = notLie.union(party) # 해당 파티 인원 더해주기

result = 0
for party in arr:
    if notLie.intersection(party): # 진실을 아는 사람이 파티에 속한 경우(여기서 진실을 아는 사람은 모든 경우의 수룰 고려한 이후)
        continue
    else: # 진실을 아는 사람이 없는 경우
        result += 1

print(result)

'''
10 9
4 1 2 3 4
2 1 5
2 2 6
1 7
1 8
2 7 8
1 9 7
1 10 9
2 3 10
1 4
'''