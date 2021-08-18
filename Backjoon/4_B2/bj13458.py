# 13458. 시험 감독

# 방법1.

N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())
result = 0

for people in arr:
    if people <= B: # B보다 작거나 같은 경우
        result += 1 # 그냥 +1
    else:
        if (people-B)/C > (people-B)//C: # C로 나눈 값 > C로 나눈 몫인 경우
            result += ((people-B)//C) + 2 # B시험관까지 +2
        else: # C로 딱 나눠 떨어지는 경우
            result += (people-B)//C + 1 # B시험관까지 + 1
print(result)

# 방법2.

N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())
result = 0

for people in arr:
    if people-B > 0: # B로 커버가 안되는 경우
        result += ((people-B-1)//C) + 1
print(result+N) # B는 무조건 필요(시험 인원은 1명 이상이므로)하므로 +N