# 2261. 가장 가까운 두 점

# 참고(https://casterian.net/archives/92)
def dist(x1, x2): # 거리구하기
    return (x1[0] - x2[0])**2 + (x1[1] - x2[1])**2

def find_dist(coords, num):
    if num == 2: # 2개인 경우
        return dist(coords[0], coords[1])
    elif num == 3: # 3개인 경우(1개와 2개인 경우로 나누는게 더 빠른 듯 함)
        return min(dist(coords[0], coords[1]), dist(coords[0], coords[2]), dist(coords[1], coords[2]))

    mid = (coords[num//2-1][0] + coords[num//2][0])//2 # 중앙선 구현(x좌표로 정렬되었으므로)
    d = min(find_dist(coords[:num//2], num//2), find_dist(coords[num//2:], num//2)) # 분할 정복

    candidate = []
    for coord in coords:
        if (mid - coord[0])**2 < d: # 중앙선과의 거리가 d보다 작은 경우(x좌표의 거리가 최소값 d보다 크면 무조건 d값보다 크게 나오므로 거름)
            candidate.append(coord)
    
    candidate.sort(key = lambda x: x[1]) # 후보들을 y좌표를 기준으로 정렬(y좌표로 비교해야 하므로)

    if len(candidate) == 0: # 후보가 없는 경우(무조건 d가 최소가 됨)
        return d
    else:
        result = d
        length = len(candidate)

        for i in range(length-1): # 같은 좌표를 비교할 필요 없으므로(범위 기억하자!)
            for j in range(i+1, length):
                if (candidate[i][1] - candidate[j][1])**2 > d: # y좌표의 거리가 d보다 큰 경우
                    break # y좌표가 가장 가까운 순서대로 나오므로 이후는 비교할 필요가 없음

                result = min(result, dist(candidate[i], candidate[j])) # 둘 중 최솟값 저장
    
    return result

import sys

input = sys.stdin.readline
N = int(input())
arr = [[] for _ in range(N)]

for i in range(N):
    arr[i] = tuple(map(int, input().split()))

arr = sorted(list(set(arr))) # 중복 제거

if len(arr) != N: # 같은 좌표가 들어온 경우
    print(0)
else: # 같은 좌표가 없는 경우
    print(find_dist(arr, N))