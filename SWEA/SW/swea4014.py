# 4014. 활주로 건설

def check(arr):
    res = 0
    for i in range(N):
        h, j = arr[i][0], 1  # 현재 높이, 시작 인덱스
        v = set()  # 중복 체크
        while j < N:
            if abs(h-arr[i][j]) > 1: break  # 높이 차이가 1이상인 경우

            elif h-arr[i][j] == 1:  # 1만큼 더 낮아진 경우
                for k in range(j, j+X):
                    if k >= N or (h-1) != arr[i][k] or k in v: break
                else:  # 활주로를 놓을 수 있는 경우
                    for k in range(j, j+X):
                        v.add(k)
                    j = k
                    h -= 1
                    continue
                break  # 활주로를 놓을 수 없는 경우

            elif h-arr[i][j] == -1:  # 1만큼 더 높아진 경우
                for k in range(j-1, j-X-1, -1):
                    if k < 0 or h != arr[i][k] or k in v: break
                else:  # 활주로를 놓을 수 있는 경우
                    for k in range(j-1, j-X-1, -1):
                        v.add(k)
                    j += 1
                    h += 1
                    continue
                break  # 활주로를 놓을 수 없는 경우

            else: j += 1  # 같은 높이인 경우

        if j == N: res += 1  # 가능한 열이면 +1
    return res


ans = []
T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    
    B = []
    for col in zip(*A):  # 열 행 뒤집기
        B.append(col)

    ans.append('#{0} {1}'.format(tc, check(A) + check(B)))

print(*ans, sep='\n')
