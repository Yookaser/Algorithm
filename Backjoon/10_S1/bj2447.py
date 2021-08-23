# 2447. 별 찍기 - 10

def stars(arr):
    x = len(arr)
    result = []
    for i in range(3*x):  # 해당 배열 길이의 3배만큼 반복
        if i // x == 1:  # 몫이 1일 때
            result.append(arr[i % x] + " " * x + arr[i % x])
        else:  # 몫이 1이 아닐 때
            result.append(arr[i % x] * 3)
    return result
 

star = ["***", "* *", "***"]  # 기본 반복요소
n = int(input())
e = 0  # 몇 번 중첩?됐는지 저장할 변수
while n != 3:
    n = n // 3
    e += 1
    
for i in range(e):  # 중첩 수만큼 반복
    star = stars(star)
for i in star:
    print(i)