# 10815. 숫자 카드

from sys import stdin


input = stdin.readline
int(input())
A = set(input().split())  # int가 아닌 str로(변환 시간 줄이기)
int(input())

print(' '.join(['1' if i in A else '0' for i in input().split()]))  # print(*list) 보다 join으로 한 번에 출력하는 게 빠름
