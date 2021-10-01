# 2112. 보호 필름

def confirm(a):  # 성능검사 함수
    for col in zip(*a):  # 열 => 행
        c = 1
        val = col[0]
        for i in col[1:]:
            if i == val: c += 1
            else:
                c = 1
                val = i
            if c >= K:  # 해당 열의 검증이 된 경우
                break
        else:  # for문이 정상 종료된 것은 검증 안 된 열이 있는 것
            return False
    return True


def combination(a):  # 조합 함수
    res = []
    for i in range(0, (1<<len(a))):
        t = []
        for j in range(0, len(a)):
            if i & (1<<j):
                t.append(a[j])
        res.append(t)
    return res


def change(a):  # 변환 함수
    t = []
    for i in combination(a):  # 바꿔야 하는 행은 서로 다른 특성으로 변경 가능함
        for j in a:
            t.append(arr[j])
            if j in i: arr[j] = AB[0]  # 열 전체를 한 번에 바꿈
            else: arr[j] = AB[1]
        if confirm(arr):
            return True
    
    for i, j in enumerate(a):  # 원상 복귀
        arr[j] = t[i]
    return False


ans = []
T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]
    AB = [[0] * W, [1] * W]

    comb = sorted(combination([i for i in range(D)]), key=lambda x: len(x))  # 길이 기준으로 정렬해야 함
    for idx in comb:
        if change(idx):  # 답을 찾은 경우(길이가 짧은 것부터 검사함)
            ans.append('#{0} {1}'.format(tc, len(idx)))
            break

print(*ans, sep='\n')
