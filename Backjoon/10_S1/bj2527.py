# 2527. 직사각형

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    if x1 > p2 or  x2 > p1 or y1 > q2 or y2 > q1: # 안 겹치는 경우
        print('d')
    elif (x1==p2 and y1==q2) or (x1==p2 and q1==y2) or (p1==x2 and q1==y2) or (p1==x2 and y1==q2): # 꼭지점인 경우
        print('c')
    # elif len(set([(x1, y1), (p1, q1), (x1, q1), (p1, y1), (x2, y2), (p2, q2), (x2, q2), (p2, y2)])) == 7: # 꼭지점인 경우
    #     print('c')
    elif (x1==p2) or (p1==x2) or (y1==q2) or (q1==y2): # 변인 경우
        print('b')
    else: # 직사각형인 경우
        print('a')