# 1764. 듣보잡

N, M = list(map(int, input().split()))
no_listen = set() # 집합 자료형
no_see = [''] * M # 리스트 자료형(미리 초기화 해놓으면 시간 복잡도 줄일 수 있음)
result = []

for n in range(N):
    no_listen.add(input())

for m in range(M):
    no_see[m] = input()
    if no_see[m] in no_listen: # no_see가 집합 자료형이므로 시간 복잡도를 줄일 수 있음
        result.append(no_see[m])

result.sort()

print(len(result), *result, sep = '\n')