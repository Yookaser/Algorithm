import random

N = int(input())

A = [i for i in range(1, 10000)]
w = random.sample(A, N)

ws = sum(w)
C = random.randrange(ws//2, ws+1)

w_str = ' '.join(map(str, w))
print(f'{N} {C} -1 {w_str}')
