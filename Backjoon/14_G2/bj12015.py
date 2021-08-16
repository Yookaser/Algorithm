# 12015. 가장 긴 증가하는 부분 수열 2

# 방법1. 이진 탐색을 구현
def binarySearch(value):
    start, end = 1, len(stack) - 1 # 시작, 끝을 지정(0번 인덱스는 0으로 필요 없음)
    while start < end: # 시작이 더 작은 경우만 반복
        mid = (start+end)//2
        if stack[mid] < value:
            start = mid + 1
        else:
            end = mid
    return end # start를 반환해도 상관은 없음


import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
stack = [0] # 비교를 위해 시작값은 0으로 넣어줌(문제 조건상 가장 작은 값은 1이므로)

for num in arr:
    if stack[-1] < num: # 스택의 끝 값보다 큰 경우(그냥 추가할 수 있음)
        stack.append(num)
    else: # 스택의 끝 값보다 작은 경우(해당 값과 가장 가까운 큰 값과 변경함 => 이해가 안되면 51~52line 예시로 시도해볼 것)
        stack[binarySearch(num)] = num

print(len(stack)-1) # -1은 초기 0을 넣어준 것을 뺀 것


# # 방법2. 이진 탐색 모듈 사용

# import sys
# from bisect import bisect_left

# input = sys.stdin.readline
# N = int(input())
# arr = list(map(int, input().split()))
# stack = [0] # 비교를 위해 시작값은 0으로 넣어줌(문제 조건상 가장 작은 값은 1이므로)

# for num in arr:
#     if stack[-1] < num: # 스택의 끝 값보다 큰 경우(그냥 추가할 수 있음)
#         stack.append(num)
#     else: # 스택의 끝 값보다 작은 경우(해당 값과 가장 가까운 큰 값과 변경함)
#         stack[bisect_left(stack, num)] = num

# print(len(stack)-1) # -1은 초기 0을 넣어준 것을 뺀 것


"""
10
100 50 70 90 75 87 105 78 110 60
"""