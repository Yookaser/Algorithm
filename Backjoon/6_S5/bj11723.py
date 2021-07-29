# 11723. 집합
import sys

input = sys.stdin.readline

T = int(input())
arr = set()

for i in range(T): # 시간 초과 문제로 인하여 class 사용 불가함
    command = input().split()

    if command[0] == 'add':
        arr.add(command[1])

    elif command[0] == 'remove':
        arr.discard(command[1])

    elif command[0] == 'check':
        if command[1] in arr:
            print(1)
        else:
            print(0)

    elif command[0] == 'toggle':
        if command[1] in arr:
            arr.discard(command[1])
        else:
            arr.add(command[1])

    elif command[0] == 'all':
        arr = set(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']) # for문이 아닌 직접 명시해서 시간 줄여야 함

    elif command[0] == 'empty':
        arr = set()