# 17779. 게리멘더링 2

def gerrymandering(x, y, d1, d2):  # if를 덜 쓰고 변수를 많이 활용하면 훨씬 빨라짐..(나중에 도전해보기)
    x1, x2, x3, x4, x5 = 0, 0, 0, 0, 0  # 리스트보다 변수가 속도가 좀 더 빠름

    ds, de = [0] * N, [0] * N  # 5번 선거구의 끝 지점, 시작 지점을 저장

    for i in range(N):
        if i < x:
            ds[i] = de[i] = y
        elif i > (x+d1+d2):
            ds[i] = de[i] = (y-d1+d2) - 1  # 5가 나오는 마지막 행의 y는 y-d1+d2로 구함 (3과 4의 범위를 고려하기 위해 -1을 추가)
        else:
            if i<= x+d1:
                ds[i] = ds[i-1] - 1  # 전꺼에서 -1(d1)
            else:
                ds[i] = ds[i-1] + 1  # 전 꺼에서 +1(d2)

            if i <= x+d2:
                de[i] = de[i-1] + 1
            else:
                de[i] = de[i-1] - 1

    for i in range(N**2):
        r, c = divmod(i, N)
        if c <= ds[r]:  # 5번 선거구 시작지점 전
            if r < x + d1:
                x1 += a[r][c]
            else:
                x3 += a[r][c]
        elif c >= de[r]:  # 5번 선거구 끝지점 후
            if r <= x + d2:
                x2 += a[r][c]
            else:
                x4 += a[r][c]
        else:  # 5번 선거구
            x5 += a[r][c]
    return max(x1, x2, x3, x4, x5) - min(x1, x2, x3, x4, x5)


N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
ans = 10**5

for x in range(1, N-2):  # x는 위 1칸, 밑 2칸을 비워야 함
    for y in range(1, N-1):  # y는 양옆 1칸을 비워야 함
        for d1 in range(1, y+1):
            for d2 in range(1, N-y):
                if d1 + d2 <= N-x:
                    ans = min(ans, gerrymandering(x, y, d1, d2))
print(ans)
