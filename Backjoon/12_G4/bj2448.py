# 2448. 별 찍기 - 11

def stars(arr):
    x = len(arr)
    result = []
    for i in range(2*x):  # 해당 배열 길이의 2배만큼 반복
        if i // x < 1:  # 몫이 1 이하일 때
            result.append(' '*x + arr[i] + ' '*x)
        else:  # 몫이 1 이상일 때
            result.append(arr[i%x] + ' ' + arr[i%x])
    return result


star = ["  *  ", " * * ", "*****"]  # 기본 반복요소
n = int(input())
e = 0  # 몇 번 중첩?됐는지 저장할 변수
while n != 3:
    n = n // 2
    e += 1

for i in range(e):  # 중첩 수만큼 반복
    star = stars(star)
for i in star:
    print(i)