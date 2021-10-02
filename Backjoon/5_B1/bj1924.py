# 1924. 2007년

week = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 각 달의 마지막 일 수

X, Y = map(int, input().split())
print(week[(sum(month[:X-1])+Y)%7])  # 각 달의 일 수들과 Y를 더하고 7로 나머지를 구함