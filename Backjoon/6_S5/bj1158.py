# 요세푸스 문제
        
N, K = list(map(int, input().split()))
N_list = list(range(1, N + 1))

idx = 0
result = []

for _ in range(N):
    idx += K - 1 # idx 인덱스 값을 찾고, pop하면 다음 인덱스에 있던 값이 idx 인덱스가 되므로 (K - 1)해야 함

    if  idx >= len(N_list): # 해당 리스트의 길이에 도달하면 나머지로 구해야 함
        idx %= len(N_list)

    result.append(N_list.pop(idx))

print('<{}>'.format(', '.join(str(i) for i in result))) # 형 변환에 join을 사용