# 10867. 중복 빼고 정렬하기

input()
A = sorted(list(set(map(int, input().split()))))  # 문자열로 정렬하면 안됨(ex => 1 2 11)
print(*A)