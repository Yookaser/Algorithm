# 5430. AC

# 방법1. 비트 마스크


# 방법2. 
for i in range(int(input())):
    command = list(input())
    N = int(input())
    arr = input()[1:-1].split(',')
    if N == 0: arr = []
    TF = True
    TF2 = True
    
    for i in command:
        if i == 'R':
            TF = not TF
        elif len(arr):
            if TF:
                arr.pop(0)
            else:
                arr.pop(-1)
        else:
            print('error')
            TF2 = False
            break
    
    if TF2: 
        if TF: print('[' + ','.join(map(str, arr)) + ']')
        else: print('[' + ','.join(map(str, arr[::-1])) + ']')