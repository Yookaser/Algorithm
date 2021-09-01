# 17140 이차원 배열과 연산

from collections import defaultdict


def make_col(arr):  # 열과 행을 뒤집는 함수
    res = []
    for col in zip(*arr):
        res.append(col)
    return res


def cal(arr, X, iscol=False):  # iscol=True => C연산
    if iscol:
        arr = make_col(arr)
    
    t1, t2 = [[] for _ in range(X)], [0] * X  # t1 => 바뀐 2차원 리스트를 저장, t2 => 바뀐 열의 길이를 저장

    for i in range(X):
        t3 = defaultdict(int)  # 초기값 0으로 만듬(Key: 해당 숫자, Value: 나온 횟수)
        for j in arr[i]:
            if not j:  # 0인 경우 그냥 지나감(break 걸면 안됨)
                continue
            t3[j] += 1
        
        for val in sorted(t3.items(), key=lambda x: (x[1], x[0])):  # value, key 순으로 정렬
            t1[i].append(val[0])  # Key 추가
            t1[i].append(val[1])  # Value 추가
        t2[i] = len(t1[i])
    
    X = max(t2)  # 길이의 최댓값 저장
    for i in range(len(t1)):
        val = X - t2[i]
        if val > 0:
            t1[i].extend([0] * val)  # 최대 길이에 맞추기

    if iscol:
        t1 = make_col(t1)
    return t1, X


r, c, k = map(int, input().split())
R, C = 3, 3
arr = [list(map(int, input().split())) for _ in range(3)]

ans = 0
for _ in range(101):  # 반드시 ans가 0과 100이 출력되게 만들어줘야함(여기서는 0을 출력하기 위해 먼저 검사를 하므로 범위는 101까지!)
    try:  # 인덱스 오류를 방지하기 위해 try ~ except 구문을 사용
        if arr[r-1][c-1] == k:
            print(ans)
            break
    except IndexError:
        pass
    if R >= C:
        arr, C = cal(arr, R)
    else:
        arr, R = cal(arr, C, True)

    ans += 1
else:
    print(-1)
