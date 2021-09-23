# 2470. 두 용액

N = int(input())
arr = sorted(map(int, input().split()))

s, e = 0, N -1
v = 10**10  # 문제 조건 상 2*(10**9) 이상이면 될 것 같음
crd = [0, 0]  # 결과 좌표

while e > s:
    t = arr[s]+arr[e]

    if abs(t) < v:
        v = abs(t)
        crd = [s, e]
    
    if t > 0:  # t가 양수였다면, 양수의 크기를 줄여 0에 근접시켜야 함
        e -= 1
    else:  # t가 음수였다면, 음수의 크기를 줄여 0에 근접시켜야 함
        s += 1

print(arr[crd[0]], arr[crd[1]])
