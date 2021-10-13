# 5644. 무선 충전

def compare(a, b):
    res = 0
    for v_a, i in a:  # 모든 경우의 수 다 찾아보기
        for v_b, j in b:
            if i == j: res = max(res, v_a)  # 충전소가 같은 경우
            else: res = max(res, v_a+v_b)  # 충전소가 다른 경우
    return res


def charge(ax, ay, bx, by):
    a, b = set(), set()  # 충전량, 충전소 번호
    for i in range(C):
        if (ay, ax) in dic[i][1]: a.add((dic[i][0], i))
        if (by, bx) in dic[i][1]: b.add((dic[i][0], i))

    if a and b: return compare(a, b)  # 둘 다 있는 경우
    elif a: return max(a)[0]  # a만 있는 경우
    elif b: return max(b)[0]  # b만 있는 경우
    else: return 0  # 둘 다 없는 경우


ans = []
dxy = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]
T = int(input())
for tc in range(1, T+1):
    M, C = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dic = {}  # key: 무선충전 번호(0~C-1), value: [충전량, 충전가능 좌표(set)]
    for i in range(C):
        x, y, c, p = map(int, input().split())
        x, y = x - 1, y - 1
        dic[i] = [p, set()]
        
        for dx in range(-c, c+1):
            for dy in range(-c, c+1):
                nx, ny = x + dx, y + dy
                if (-1<nx<10) and (-1<ny<10) and abs(nx-x) + abs(ny-y) <= c:  # 범위내이고 충전소 거리 이내인 경우
                    dic[i][1].add((ny, nx))

    ax, ay, bx, by = 0, 0, 9, 9  # 시작 좌표
    res = charge(ax, ay, bx, by)  # 시작 좌표의 충전량
    for i in range(M):
        dax, day = dxy[A[i]]
        dbx, dby = dxy[B[i]]
        ax, ay, bx, by = ax + dax, ay + day, bx + dbx, by + dby  # 좌표 이동
        res += charge(ax, ay, bx, by)  # 해당 좌표의 충전량을 합
    
    ans.append('#{0} {1}'.format(tc, res))

print(*ans, sep='\n')
