# 5373. 큐빙

def rotation(arr, d):
    temp = [[0] * 3 for _ in range(3)]

    if d == 1:
        for i in range(9):
            r, c = divmod(i, 3)
            temp[r][c] = arr[2-c][r]
    else:
        for i in range(9):
            r, c = divmod(i, 3)
            temp[r][c] = arr[c][2-r]
    return temp


def column(arr, idx):
    result = []
    for i in range(3):
        result.append(arr[i][idx])
    return result


T = int(input())
for _ in range(T):
    N = int(input())
    arr = input().split()
    
    U = [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
    D = [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]
    F = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]
    B = [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]
    L = [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]
    R = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]

    for value in arr:
        h, d  = value[0], value[1]
        if h == 'U':
            if d == '+':
                L[0], F[0], R[0], B[0] = F[0], R[0], B[0], L[0]
                U = rotation(U, 0)
            else:
                L[0], F[0], R[0], B[0] = B[0], L[0], F[0], R[0]
                U = rotation(U, 1)
        elif h == 'D':
            if d == '+':
                L[2], F[2], R[2], B[2] = F[2], R[2], B[2], L[2]
                D = rotation(D, 0)
            else:
                L[2], F[2], R[2], B[2] = B[2], L[2], F[2], R[2]
                D = rotation(D, 1)


        elif h == 'L':
            if d == '+':
                for i in range(3):
                    
                    U[i][0], F[i][0], D[i][0], B[i][0] = B[i][0], U[i][0], F[i][0], D[i][0]
                L = rotation(L, 0)
            else:
                for i in range(3):
                    U[i][0], F[i][0], D[i][0], B[i][0] = F[i][0], D[i][0], B[i][0], U[i][0]
                L = rotation(L, 1)
        elif h == 'F':
            if d == '+':
                for i in range(3):
                    L[i][2], U[2][i], R[i][0], D[0][i] = D[0][i], L[2][i], U[2][i], R[i][0]
                F = rotation(F, 0)
            else:
                for i in range(3):
                    L[i][2], U[2][i], R[i][0], D[0][i] = U[2][i], R[i][0], D[0][i], L[i][2]
                F = rotation(F, 1)
        elif h == 'R':
            if d == '+':
                for i in range(3):                   
                    U[i][2], F[i][2], D[i][2], B[i][2] = F[i][2], D[i][2], B[i][2], U[i][2]
                R = rotation(R, 0)
            else:
                for i in range(3):
                    U[i][2], F[i][2], D[i][2], B[i][2] = B[i][2], U[i][2], F[i][2], D[i][2]
                R = rotation(R, 1)
        elif h == 'B':
            if d == '+':
                for i in range(3):
                    L[i][0], U[0][i], R[i][2], D[2][i] = U[0][i], R[i][2], D[2][i], L[i][0]
                B = rotation(B, 0)
            else:
                for i in range(3):
                    L[i][0], U[0][i], R[i][2], D[2][i] = D[2][i], L[i][0], U[0][i], R[i][2]
                B = rotation(B, 1)

    for i in range(3):
        print(''.join(U[i]))

    print('\n')

    print('U', U)
    print('D', D)
    print('F', F)
    print('B', B)
    print('L', L)
    print('R', R)




def rotation(arr, d):
    temp = [[0] * 3 for _ in range(3)]

    if d == 1:
        for i in range(9):
            r, c = divmod(i, 3)
            temp[r][c] = arr[2-c][r]
    else:
        for i in range(9):
            r, c = divmod(i, 3)
            temp[r][c] = arr[c][2-r]
    return temp


U = [['w'] * 3 for _ in range(3)]
D = [['y'] * 3 for _ in range(3)]
F = [['r'] * 3 for _ in range(3)]
B = [['o'] * 3 for _ in range(3)]
L = [['g'] * 3 for _ in range(3)]
R = [['b'] * 3 for _ in range(3)]

def change(area, d):  # 면, 방향
    if area == 'U':
        a, b, c, d, e = U, L, F, R, B
    elif area == 'D':
        a, b, c, d, e = D, L, F, R, B
    elif area == 'L':
        a, b, c, d, e = L, U, F, D, B
    elif area == 'F':
        a, b, c, d, e = F, L, U, R, D
    elif area == 'R':
        a, b, c, d, e = R, U, F, D, B
    elif area == 'B':
        a, b, c, d, e = B, L, U, R, D
    
    

    if area in ('U', 'D'):
        if d =='+':
            b[0], c[0], d[0], e[0] = c[0], d[0], e[0], b[0]
        else:
            b[0], c[0], d[0], e[0] = e[0], b[0], c[0], d[0]
    else:
        if d =='+':
            b[0][0], b[1][0], b[2][0], c[0][0], c[1][0], c[2][0], \
            d[0][0], d[1][0], d[2][0], e[0][0], e[1][0], e[2][0] = \
            


    a = rotation(a, '+') if d == '+' else rotation(a, '-')