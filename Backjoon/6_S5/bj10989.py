# 10989. 수 정렬하기 3

import sys

input = sys.stdin.readline

N = int(input())
arr = [0] * 10001 # 인덱스 번호가 해당 숫자를, 요소가 개수를 의미

for i in range(N):
    arr[int(input())] += 1 # 해당 인덱스에 +1

for i in range(1, 10001): # 출력하기 위해 2중 for문
    for j in range(arr[i]): # 0이면 자동으로 안 돌게 됨
        print(i)