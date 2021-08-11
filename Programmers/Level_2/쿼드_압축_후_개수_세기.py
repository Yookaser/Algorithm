# 쿼드 압축 후 개수 세기

# 방법1.
def solution(arr):
    zero = 0 # 0을 카운트
    own = 0 # 1을 카운트
    
    def alzip(arr, N):
        nonlocal zero, own
        if N == 1: # base case
            if arr[0][0]: # 1인 경우
                own += 1
            else: # 0인 경우
                zero += 1
            return
        elif sum(sum(arr, [])) == 0 or sum(sum(arr, [])) == N**2: # 블럭이 같은 값인 경우
            if sum(sum(arr, [])): # 0인 경우
                own += 1
            else: # 1인 경우
                zero += 1
            return
            
        new_arr1 = []
        new_arr2 = []
        new_arr3 = []
        new_arr4 = []
        for i in range(N): # 4개로 분리
            if i < N//2:
                new_arr1.append(arr[i][:N//2])
                new_arr2.append(arr[i][N//2:])
            else:
                new_arr3.append(arr[i][:N//2])
                new_arr4.append(arr[i][N//2:])
                
        alzip(new_arr1, N//2) # 재귀
        alzip(new_arr2, N//2)
        alzip(new_arr3, N//2)
        alzip(new_arr4, N//2)
    
    alzip(arr, len(arr))
    return [zero, own]

# 방법2.
# def solution(arr):
#     result = [0, 0] # 0, 1의 개수(리스트 요소는 함수에서 수정 가능하므로 리스트로 저장)

#     def alzip(x, y, size):
#         if size == 1: # base case
#             result[arr[x][y]] += 1 # 해당 좌표의 값(인덱스) +1
#             return
#         else:
#             confirm = arr[x][y] # 확인용 변수

#             for dx in range(size):
#                 for dy in range(size):
#                     if confirm != arr[x+dx][y+dy]: # dx, dy를 더해주는 방향으로 가야됨(왜냐면 x, y를 매개변수로 쓰므로)
#                         alzip(x, y, size//2)
#                         alzip(x + size//2, y, size//2)
#                         alzip(x, y + size//2, size//2)
#                         alzip(x + size//2, y + size//2, size//2)
#                         return
#             result[confirm] += 1 # 만약, for문 전체를 돌았다면 confirm(인덱스) +1(모두 같은 값인 경우)
#     alzip(0, 0, len(arr))
#     return result