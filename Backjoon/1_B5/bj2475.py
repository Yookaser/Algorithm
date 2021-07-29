# 2475. 검증수

arr = list(map(int, input().split()))

result = sum(list(map(lambda x: x**2, arr))) % 10 # map, lambda 이용
print(result)