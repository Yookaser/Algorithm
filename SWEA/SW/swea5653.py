# 5653. 줄기세포배양

from collections import defaultdict


ans = []
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    d_c = set()  # 죽은 셀의 좌표 저장(중복 방지)
    w_c = defaultdict(dict)  # key: 활성 시간 | value: 딕셔너리 => key: 크기 | value: 좌표
    a_c = defaultdict(dict)  # key: 죽는 시간 | value: 딕셔너리 => key: 크기 | value: 좌표
    for i in range(N*M):  # 초기 상태의 대기 세포 갱신
        r, c = divmod(i, M)
        if A[r][c]:
            d_c.add((r, c))  # 중복 방지를 위해 미리 추가
            if A[r][c] in w_c[A[r][c]]:
                w_c[A[r][c]][A[r][c]].add((r, c))
            else:
                w_c[A[r][c]][A[r][c]] = set([(r, c)])

    for i in range(1, K+1):
        go = dict()
        for k, v in a_c.items():  # 활성화된 세포 중 번식 가능 좌표 확인
            for vk, vv in v.items():
                for x, y in vv:
                    for nx, ny in ((x-1, y), (x, y+1), (x+1, y), (x, y-1)):
                        if (nx, ny) in d_c: continue
                        if (nx, ny) in go:
                            go[(nx, ny)] = max(go[(nx, ny)], vk)
                        else:
                            go[(nx, ny)] = vk

        if i in a_c: del a_c[i]  # 활설화 끝난 세포의 딕셔너리 제거
        
        for k, v in go.items():  # 세포 번식
            d_c.add(k)  # 중복 방지를 위해 미리 추가
            if v in w_c[i+v]: w_c[i+v][v].add(k)
            else: w_c[i+v][v] = set([k])

        if i in w_c:  # 대기 세포를 활성화 세포로 생성
            for k, v in w_c[i].items():
                if k in a_c[i+k]:
                    a_c[i+k][k] |= v
                else:
                    a_c[i+k][k] = v
            del w_c[i]
    
    res = 0
    for k, v in w_c.items():
        for kk, vv in v.items():
            res += len(vv)
    
    for k, v in a_c.items():
        for kk, vv in v.items():
            res += len(vv)

    ans.append('#{0} {1}'.format(tc, res))

print(*ans, sep='\n')
