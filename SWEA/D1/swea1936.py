# 1936. 1대1 가위바위보

def game(p1, p2, op1, op2):
    if op1 == 1 and op2 == 3:
        return print(p1)
    elif op1 == 2 and op2 == 1:
        return print(p1)
    elif op1 == 3 and op2 == 2:
        return print(p1)
    else:
        return print(p2)

arr = list(map(int, input().split()))
A, B = arr[0], arr[1]
game('A', 'B', A, B)