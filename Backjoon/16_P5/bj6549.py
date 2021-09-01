# 6549. 히스토그램에서 가장 큰 직사각형

import sys


input = sys.stdin.readline
while True:
    arr = list(map(int, input().split()))
    n = arr.pop(0)
    if(n == 0): break
    
    arr.insert(0, 0)
    arr.append(0)
    checked = [0]
    area = 0
    
    for i in range(1, n + 2):
        while(checked and (arr[checked[-1]] > arr[i])):
            cur_height = checked.pop()
            area = max(area, (i - 1 - checked[-1]) * arr[cur_height])
        checked.append(i)
    print(area)
